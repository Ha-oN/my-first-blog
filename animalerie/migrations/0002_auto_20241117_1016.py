# Generated by Django 2.2.28 on 2024-11-17 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animalerie', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='team',
            new_name='couleur',
        ),
        migrations.RemoveField(
            model_name='character',
            name='type',
        ),
    ]
