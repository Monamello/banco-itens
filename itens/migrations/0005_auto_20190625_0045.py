# Generated by Django 2.2 on 2019-06-25 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itens', '0004_auto_20190623_0410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='suporte',
        ),
        migrations.AddField(
            model_name='item',
            name='suporte_imagem',
            field=models.ImageField(blank=True, null=True, upload_to='imagem_alternativas'),
        ),
        migrations.AddField(
            model_name='item',
            name='suporte_texto',
            field=models.TextField(blank=True, max_length=1200, null=True),
        ),
    ]
