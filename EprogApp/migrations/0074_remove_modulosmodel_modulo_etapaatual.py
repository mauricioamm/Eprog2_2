# Generated by Django 3.2.7 on 2022-07-29 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EprogApp', '0073_modulosmodel_modulo_etapaatual'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modulosmodel',
            name='Modulo_EtapaAtual',
        ),
    ]
