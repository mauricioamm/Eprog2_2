# Generated by Django 3.0.6 on 2020-05-16 04:02

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EprogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Topico', models.CharField(blank=True, max_length=1000)),
                ('Textao', models.CharField(blank=True, max_length=1000)),
                ('OndeFigura1', models.CharField(blank=True, max_length=200)),
                ('DuvidaComent', models.CharField(blank=True, max_length=500)),
            ],
            managers=[
                ('objetos', django.db.models.manager.Manager()),
            ],
        ),
    ]
