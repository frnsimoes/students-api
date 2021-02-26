# Generated by Django 3.0.5 on 2021-02-26 00:38

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('idade_ate_31_12_2016', models.CharField(max_length=20)),
                ('ra', models.CharField(max_length=15)),
                ('campus', models.CharField(max_length=2)),
                ('curso', models.CharField(max_length=50)),
                ('modalidade', models.CharField(max_length=50)),
                ('nivel_do_curso', models.CharField(max_length=50)),
                ('data_inicio', models.DateField()),
            ],
        ),
    ]