# Generated by Django 3.0.6 on 2020-05-24 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EprogApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eprogmodel',
            name='DuvidaComent',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='eprogmodel',
            name='OndeFigura1',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='eprogmodel',
            name='Textao',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='eprogmodel',
            name='Topico',
            field=models.CharField(max_length=1000),
        ),
    ]
