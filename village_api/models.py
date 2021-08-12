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


class Location(models.Model):
    name = models.CharField(max_length=256)
    location_type = models.CharField(
        max_length=50, choices=LocationTypeChoice.to_choices_list()
    )


class Family(models.Model):
    location = models.ForeignKey(Location, on_delete=CASCADE, related_name="families")
    family_name = models.CharField(max_length=50, null=True)


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
    family = models.ForeignKey(
        Family, on_delete=CASCADE, related_name="members", null=True
    )
    location = models.ForeignKey(
        Location, on_delete=CASCADE, related_name="people", null=True
    )
