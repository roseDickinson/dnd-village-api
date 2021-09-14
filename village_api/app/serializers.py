from django.contrib.auth.models import User
from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers

from village_api.models import (
    Person,
    Location,
    Relationship,
    Relation,
    RelationshipTypeChoice,
    StatusChoice,
)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class RelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relationship
        fields = "__all__"


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"


class PersonBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        exclude = ["location", "siblings", "parents"]


class LocationBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class GraphDataSerializer(serializers.Serializer):
    nodes = serializers.JSONField()
    links = serializers.JSONField()


def add_links(source, value, relationship_list, links, color):
    for target in relationship_list:
        key = f"{source}->{target}"
        potential_dupe_key = f"{target}->{source}"
        if potential_dupe_key in links:
            continue
        links[key] = {
            "source": source,
            "target": target,
            "value": value,
            "color": color,
        }


class LocationSerializer(serializers.ModelSerializer):
    people = serializers.SerializerMethodField("get_people")
    graph_data = serializers.SerializerMethodField("get_graph_data")

    class Meta:
        model = Location
        fields = "__all__"

    @swagger_serializer_method(serializer_or_field=PersonBasicSerializer(many=True))
    def get_people(self, instance):
        return PersonBasicSerializer(instance.people, many=True).data

    @swagger_serializer_method(serializer_or_field=GraphDataSerializer(many=True))
    def get_graph_data(self, instance):
        people = Person.objects.filter(location=instance.id)

        links = {}
        nodes = []
        for person in people:
            color = "green"
            if person.status == StatusChoice.DEAD.value:
                color = "black"
            if person.status == StatusChoice.MISSING.value:
                color = "blue"
            if person.status == StatusChoice.UNKNOWN.value:
                color = "grey"
            nodes.append(
                {
                    "id": str(person.id),
                    "name": person.name,
                    "group": person.family_name,
                    "color": color,
                }
            )
            source = str(person.id)
            add_links(source, 75, person.parents, links, "cyan")
            add_links(source, 50, person.siblings, links, "blue")
            relationships = person.relationships.all()
            romantic_relations = []
            friendships = []
            enemies = []
            acquantances = []
            for relation in relationships:
                other_people = relation.people.exclude(id=person.id)
                for other_person in other_people:
                    if relation.type == RelationshipTypeChoice.ROMANTIC.value:
                        romantic_relations.append(str(other_person.id))
                    if relation.type == RelationshipTypeChoice.FRIENDSHIP.value:
                        friendships.append(str(other_person.id))
                    if relation.type == RelationshipTypeChoice.ENEMY.value:
                        enemies.append(str(other_person.id))
                    if relation.type == RelationshipTypeChoice.ACQUAINTANCE.value:
                        acquantances.append(str(other_person.id))
            add_links(source, 25, romantic_relations, links, "hotpink")
            add_links(source, 125, friendships, links, "green")
            add_links(source, 125, enemies, links, "red")
            add_links(source, 150, acquantances, links, "grey")

        return GraphDataSerializer({"nodes": nodes, "links": links.values()}).data
