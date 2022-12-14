# Generated by Django 4.0.6 on 2022-10-06 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nit', models.CharField(max_length=9)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido1', models.CharField(max_length=100)),
                ('apellido2', models.CharField(max_length=100)),
                ('código_departamento', models.IntegerField()),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
    ]
