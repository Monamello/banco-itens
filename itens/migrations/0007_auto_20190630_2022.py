# Generated by Django 2.2 on 2019-06-30 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itens', '0006_auto_20190630_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alternativa',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='static'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='unidades_curriculares',
            field=models.ManyToManyField(related_name='cursos', to='itens.UnidadeCurricular'),
        ),
        migrations.AlterField(
            model_name='item',
            name='suporte_imagem',
            field=models.ImageField(blank=True, null=True, upload_to='static'),
        ),
    ]