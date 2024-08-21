# Generated by Django 4.2.6 on 2024-07-29 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turmas', '0009_remove_turma_usuario'),
        ('usuario', '0004_remove_usuario_turma'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='turma',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alunos', to='turmas.turma'),
        ),
    ]
