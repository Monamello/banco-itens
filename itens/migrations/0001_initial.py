# Generated by Django 2.2 on 2019-06-23 03:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=254)),
                ('docente', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UnidadeCurricular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciado', models.CharField(max_length=500)),
                ('suporte', models.CharField(max_length=500)),
                ('comando', models.CharField(max_length=500)),
                ('dificuldade', models.CharField(choices=[('muito_facil', 'Muito Fácil'), ('facil', 'Fácil'), ('medio', 'Médio'), ('dificil', 'Difícil'), ('muito_dificil', 'Muito Difícil')], max_length=30)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('cursos', models.ManyToManyField(to='itens.Cursos')),
                ('unidades_curriculares', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unidades_curriculares', to='itens.UnidadeCurricular')),
            ],
        ),
        migrations.AddField(
            model_name='cursos',
            name='unidades_curriculares',
            field=models.ManyToManyField(to='itens.UnidadeCurricular'),
        ),
        migrations.CreateModel(
            name='Alternativa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=500)),
                ('imagem', models.ImageField(upload_to='imagem_alternativas')),
                ('correta', models.BooleanField(default=False)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alternativas', to='itens.Item')),
            ],
        ),
    ]
