# Generated by Django 3.2.7 on 2022-07-16 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EprogApp', '0058_auto_20220715_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procedimentomodel',
            name='Acesso01_preteste',
            field=models.TextField(blank=True, default='1', max_length=3),
        ),
        migrations.AlterField(
            model_name='procedimentomodel',
            name='Acesso01_treino',
            field=models.TextField(blank=True, default='1', max_length=3),
        ),
        migrations.AlterField(
            model_name='procedimentomodel',
            name='Etapa01',
            field=models.TextField(blank=True, default='1', max_length=3),
        ),
    ]
