# Generated by Django 3.2.6 on 2021-09-05 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('village_api', '0008_alter_relationship_people'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='extra_info',
            field=models.TextField(default=''),
        ),
    ]