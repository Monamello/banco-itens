# Generated by Django 2.2 on 2019-06-18 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itens', '0004_auto_20190502_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='alternativas',
        ),
        migrations.AddField(
            model_name='alternativa',
            name='item',
            field=models.ForeignKey(default=1, on_delete='CASCADE', related_name='alternativas', to='itens.Item'),
            preserve_default=False,
        ),
    ]
