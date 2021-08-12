from django.contrib.auth.models import User
from rest_framework import generics, permissions, viewsets

from village_api.models import Family, Location, Person
from village_api.app.serializers import (
    FamilySerializer,
    LocationSerializer,
    PersonSerializer,
    UserSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class Familys(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Family.objects.all()
    serializer_class = FamilySerializer
    permission_classes = [permissions.IsAuthenticated]


class Locations(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]


class Persons(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticated]
