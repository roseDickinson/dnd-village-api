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


class LocationSerializer(serializers.ModelSerializer):
    people = serializers.SerializerMethodField("get_people")

    class Meta:
        model = Location
        fields = "__all__"

    @swagger_serializer_method(serializer_or_field=PersonBasicSerializer(many=True))
    def get_people(self, instance):
        people = Person.objects.filter(location=instance.id)

        return PersonBasicSerializer(people, many=True).data
