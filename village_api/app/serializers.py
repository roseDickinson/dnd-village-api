from django.contrib.auth.models import User
from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers

from village_api.models import Person, Location, Relationship


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
        fields = ["id", "name", "status", "parents", "siblings"]


class LocationBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class GraphDataSerializer(serializers.Serializer):
    nodes = serializers.JSONField()
    links = serializers.JSONField()


def add_links(source, relationship_list, links):
    for target in relationship_list:
        key = f"{source}->{target}"
        potential_dupe_key = f"{target}->{source}"
        if potential_dupe_key in links:
            return
        links[key] = {"source": source, "target": target, "value": 2}


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
            nodes.append(
                {
                    "id": str(person.id),
                    "group": person.family_name,
                    "radius": 5,
                }
            )
            source = str(person.id)
            add_links(source, person.parents, links)
            add_links(source, person.siblings, links)

        return GraphDataSerializer({"nodes": nodes, "links": links.values()}).data
