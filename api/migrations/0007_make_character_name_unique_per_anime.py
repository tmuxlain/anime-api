# Generated by Django 2.0.8 on 2018-12-15 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_make_character_name_unique'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='character',
            unique_together={('name', 'anime')},
        ),
    ]