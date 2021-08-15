from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models.deletion import CASCADE

from village_api.app.DjangoChoicesEnum import DjangoChoicesEnum


class RaceChoice(DjangoChoicesEnum):
    AASIMAR = "Aasimar"
    HUMAN = "Human"
    LOXODON = "Loxodon"
    TIEFLING = "Tiefling"
    VEDALKEN = "Vedalken"


class GenderChoice(DjangoChoicesEnum):
    AGENDER = "Agender"
    CIS_MAN = "Cis man"
    CIS_WOMAN = "Cis woman"
    ENBY = "Nonbinary"
    TRANS_MAN = "Trans man"
    TRANS_WOMAN = "Trans woman"


class SexualityChoice(DjangoChoicesEnum):
    ACE = "Asexual"
    ARO = "Aromantic"
    BI = "Bisexual"
    GAY = "Gay"
    HET = "Heterosexual"
    LES = "Lesbian"
    PAN = "Pansexual"


class StatusChoice(DjangoChoicesEnum):
    ALIVE = "Alive"
    DEAD = "Dead"
    MISSING = "Missing"
    UNKNOWN = "Unknown"


class LocationTypeChoice(DjangoChoicesEnum):
    V = "Village"
    C = "City"
    D = "Dungeon"


class RelationshipTypeChoice(DjangoChoicesEnum):
    ROMANTIC = "Romantic"
    FRIENDSHIP = "Friends"
    ENEMY = "Enemies"
    ACQUAINTANCE = "Acquaintances"


class Location(models.Model):
    name = models.CharField(max_length=256)
    location_type = models.CharField(
        max_length=50, choices=LocationTypeChoice.to_choices_list()
    )


class Person(models.Model):
    race = models.CharField(max_length=50, choices=RaceChoice.to_choices_list())
    gender = models.CharField(max_length=50, choices=GenderChoice.to_choices_list())
    sexuality = models.CharField(
        max_length=50, choices=SexualityChoice.to_choices_list()
    )
    age = models.CharField(max_length=10)
    name = models.CharField(max_length=256)
    status = models.CharField(max_length=50, choices=StatusChoice.to_choices_list())
    profession = models.CharField(max_length=256)
    location = models.ForeignKey(
        Location, on_delete=CASCADE, related_name="people", null=True
    )
    siblings = models.ManyToManyField("self")
    # Can't seem to find a way to properly create a list of Person
    # objects so just gonna list ids and manually look them up
    parents = ArrayField(
        models.CharField(max_length=50),
        default=list,
    )


class Relationship(models.Model):
    people = models.ManyToManyField(Person, related_name="relationships")
    type = models.CharField(
        max_length=100, choices=RelationshipTypeChoice.to_choices_list()
    )
    details = models.CharField(max_length=1000)
