# Generated by Django 5.0.4 on 2024-07-14 14:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turmas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turma',
            name='alunos',
        ),
        migrations.AddField(
            model_name='turma',
            name='alunos',
            field=models.ForeignKey(blank=True, limit_choices_to={'tipo': 'ALUNO'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='turmas_aluno', to=settings.AUTH_USER_MODEL),
        ),
    ]
