# Generated by Django 3.2.6 on 2021-08-10 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race', models.CharField(choices=[('Aasimar', 'AASIMAR'), ('Human', 'HUMAN'), ('Loxodon', 'LOXODON'), ('Tiefling', 'TIEFLING'), ('Vedalken', 'VEDALKEN')], max_length=50)),
                ('gender', models.CharField(choices=[('Agender', 'AGENDER'), ('Cis man', 'CIS_MAN'), ('Cis woman', 'CIS_WOMAN'), ('Nonbinary', 'ENBY'), ('Trans man', 'TRANS_MAN'), ('Trans woman', 'TRANS_WOMAN')], max_length=50)),
                ('sexuality', models.CharField(choices=[('Asexual', 'ACE'), ('Aromantic', 'ARO'), ('Bisexual', 'BI'), ('Gay', 'GAY'), ('Heterosexual', 'HET'), ('Lesbian', 'LES'), ('Pansexual', 'PAN')], max_length=50)),
                ('age', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=256)),
                ('status', models.CharField(choices=[('Alive', 'ALIVE'), ('Dead', 'DEAD'), ('Missing', 'MISSING'), ('Unknown', 'UNKNOWN')], max_length=50)),
                ('profession', models.CharField(max_length=256)),
            ],
        ),
    ]
