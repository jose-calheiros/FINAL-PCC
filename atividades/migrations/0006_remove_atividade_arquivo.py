# Generated by Django 4.2.6 on 2024-08-21 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atividades', '0005_alter_atividade_arquivo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atividade',
            name='arquivo',
        ),
    ]
