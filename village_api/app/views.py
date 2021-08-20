from django.contrib.auth.models import User
from rest_framework import generics, permissions, viewsets

from village_api.models import Location, Person, Relationship
from village_api.app.serializers import (
    LocationBasicSerializer,
    LocationSerializer,
    PersonSerializer,
    RelationshipSerializer,
    UserSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class Relationships(generics.ListCreateAPIView):
    """
    API endpoint that allows relationships to be added or listed
    """

    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer
    permission_classes = [permissions.IsAuthenticated]


class Locations(generics.ListCreateAPIView):
    """
    API endpoint that allows locations to be added or listed
    """

    queryset = Location.objects.all()
    serializer_class = LocationBasicSerializer
    permission_classes = [permissions.IsAuthenticated]


class LocationId(generics.RetrieveAPIView):
    """
    API endpoint that allows location details to be retrieved
    """

    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"


class Persons(generics.ListCreateAPIView):
    """
    API endpoint that allows persons to be added or listed
    """

    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticated]
