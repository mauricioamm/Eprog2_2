# Generated by Django 3.2.7 on 2022-07-29 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EprogApp', '0081_auto_20220729_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulosmodel',
            name='Delineamento',
            field=models.CharField(blank=True, default='1', max_length=3),
        ),
    ]
