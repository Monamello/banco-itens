# Generated by Django 2.2 on 2019-06-23 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itens', '0002_auto_20190623_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alternativa',
            name='texto',
            field=models.TextField(max_length=1200),
        ),
        migrations.AlterField(
            model_name='item',
            name='comando',
            field=models.TextField(max_length=1200),
        ),
        migrations.AlterField(
            model_name='item',
            name='enunciado',
            field=models.TextField(max_length=1200),
        ),
        migrations.AlterField(
            model_name='item',
            name='suporte',
            field=models.TextField(max_length=1200),
        ),
    ]
