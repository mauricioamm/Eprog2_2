# Generated by Django 3.2.7 on 2022-06-23 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EprogApp', '0044_alter_pretestemodel_escolheu'),
    ]

    operations = [
        migrations.AddField(
            model_name='pretestemodel',
            name='Alternativa_A_escolhida',
            field=models.CharField(blank=True, default='0', max_length=3),
        ),
        migrations.AddField(
            model_name='pretestemodel',
            name='Alternativa_B_escolhida',
            field=models.CharField(blank=True, default='0', max_length=3),
        ),
        migrations.AddField(
            model_name='pretestemodel',
            name='Alternativa_C_escolhida',
            field=models.CharField(blank=True, default='0', max_length=3),
        ),
        migrations.AddField(
            model_name='pretestemodel',
            name='Alternativa_D_escolhida',
            field=models.CharField(blank=True, default='0', max_length=3),
        ),
        migrations.AddField(
            model_name='pretestemodel',
            name='Alternativa_E_escolhida',
            field=models.CharField(blank=True, default='0', max_length=3),
        ),
    ]
