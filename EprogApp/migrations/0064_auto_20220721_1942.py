# Generated by Django 3.2.7 on 2022-07-21 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EprogApp', '0063_procedimentomodel_etapaatual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postestemodel',
            name='Alternativa_A',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='postestemodel',
            name='Alternativa_B',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='postestemodel',
            name='Alternativa_C',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='postestemodel',
            name='Alternativa_D',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='postestemodel',
            name='Alternativa_E',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='postestemodel',
            name='Alternativa_X',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='postestemodel',
            name='Questao',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
    ]
