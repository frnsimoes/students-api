# Generated by Django 3.0.5 on 2021-02-26 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='municipio',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='students',
            name='nome',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='students',
            name='campus',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='students',
            name='curso',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='students',
            name='idade_ate_31_12_2016',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='students',
            name='modalidade',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='students',
            name='nivel_do_curso',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='students',
            name='ra',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]