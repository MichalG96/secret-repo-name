# Generated by Django 3.2.3 on 2021-05-30 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_pokemons', '0007_alter_pokemon_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='total',
        ),
    ]
