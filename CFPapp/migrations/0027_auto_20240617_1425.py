# Generated by Django 3.2.18 on 2024-06-17 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CFPapp', '0026_cfp_infos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='utilisateur_infos',
            name='created_by',
        ),
        migrations.DeleteModel(
            name='Villes',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Utilisateur_infos',
        ),
    ]
