# Generated by Django 3.2.7 on 2022-07-26 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EprogApp', '0066_procedimentomodel_condicao'),
    ]

    operations = [
        migrations.AddField(
            model_name='postestemodel',
            name='Numero_Posteste',
            field=models.CharField(blank=True, default='1', max_length=3),
        ),
        migrations.AddField(
            model_name='postestemodel',
            name='Posteste_Atual',
            field=models.CharField(blank=True, default='1', max_length=3),
        ),
    ]