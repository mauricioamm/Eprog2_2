# Generated by Django 3.2.7 on 2022-06-18 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EprogApp', '0030_auto_20220615_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='procedimentomodel',
            name='ModuloContinuar',
            field=models.CharField(blank=True, default='1', max_length=3),
        ),
    ]
