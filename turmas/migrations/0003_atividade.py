# Generated by Django 5.0.6 on 2024-07-23 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turmas', '0002_remove_turma_alunos_turma_alunos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
