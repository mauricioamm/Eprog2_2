# Generated by Django 3.2.7 on 2022-06-19 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EprogApp', '0033_auto_20220618_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='procedimentomodel',
            name='Retreino',
            field=models.TextField(blank=True, default='0', max_length=3),
        ),
    ]
