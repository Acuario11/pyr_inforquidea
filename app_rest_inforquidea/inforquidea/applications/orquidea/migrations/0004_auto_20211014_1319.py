# Generated by Django 3.2.8 on 2021-10-14 18:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orquidea', '0003_auto_20211014_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orquidea',
            name='duracion_flor',
            field=models.CharField(default='-', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orquidea',
            name='floracion',
            field=models.CharField(default='-', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orquidea',
            name='nombre_comun',
            field=models.CharField(default='-', max_length=30, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orquidea',
            name='tamaño_flor',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='orquidea',
            name='tipo_crecimiento',
            field=models.CharField(default='-', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orquidea',
            name='ubicacion',
            field=models.CharField(default=django.utils.timezone.now, max_length=60),
            preserve_default=False,
        ),
    ]
