# Generated by Django 4.2.6 on 2024-08-21 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0013_remove_experimento_participantes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experimento',
            name='n_maquina',
            field=models.IntegerField(),
        ),
    ]
