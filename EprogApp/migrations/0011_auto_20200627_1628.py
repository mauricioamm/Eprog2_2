# Generated by Django 3.0.6 on 2020-06-27 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EprogApp', '0010_eprogmodel_ativada'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eprogmodel',
            old_name='participante',
            new_name='Participante',
        ),
    ]
