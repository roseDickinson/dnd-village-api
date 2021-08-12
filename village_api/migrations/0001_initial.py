# Generated by Django 3.2.6 on 2021-08-12 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [
        ("village_api", "0001_initial"),
        ("village_api", "0002_auto_20210811_2019"),
        ("village_api", "0003_person_location"),
        ("village_api", "0004_auto_20210812_2127"),
    ]

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256)),
                (
                    "location_type",
                    models.CharField(
                        choices=[("Village", "V"), ("City", "C"), ("Dungeon", "D")],
                        max_length=50,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Family",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="families",
                        to="village_api.location",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "race",
                    models.CharField(
                        choices=[
                            ("Aasimar", "AASIMAR"),
                            ("Human", "HUMAN"),
                            ("Loxodon", "LOXODON"),
                            ("Tiefling", "TIEFLING"),
                            ("Vedalken", "VEDALKEN"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("Agender", "AGENDER"),
                            ("Cis man", "CIS_MAN"),
                            ("Cis woman", "CIS_WOMAN"),
                            ("Nonbinary", "ENBY"),
                            ("Trans man", "TRANS_MAN"),
                            ("Trans woman", "TRANS_WOMAN"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "sexuality",
                    models.CharField(
                        choices=[
                            ("Asexual", "ACE"),
                            ("Aromantic", "ARO"),
                            ("Bisexual", "BI"),
                            ("Gay", "GAY"),
                            ("Heterosexual", "HET"),
                            ("Lesbian", "LES"),
                            ("Pansexual", "PAN"),
                        ],
                        max_length=50,
                    ),
                ),
                ("age", models.CharField(max_length=10)),
                ("name", models.CharField(max_length=256)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Alive", "ALIVE"),
                            ("Dead", "DEAD"),
                            ("Missing", "MISSING"),
                            ("Unknown", "UNKNOWN"),
                        ],
                        max_length=50,
                    ),
                ),
                ("profession", models.CharField(max_length=256)),
                (
                    "family",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="members",
                        to="village_api.family",
                    ),
                ),
                (
                    "location",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="people",
                        to="village_api.location",
                    ),
                ),
            ],
        ),
    ]
