# Generated by Django 3.2.7 on 2022-06-24 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EprogApp', '0045_auto_20220623_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pretestemodel',
            name='name',
        ),
        migrations.AlterField(
            model_name='pretestemodel',
            name='Escolheu',
            field=models.CharField(blank=True, default='', max_length=3),
        ),
    ]