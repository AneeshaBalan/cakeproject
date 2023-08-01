# Generated by Django 4.1.7 on 2023-03-19 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CakeBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('flavour', models.CharField(max_length=250)),
                ('price', models.PositiveIntegerField()),
                ('shape', models.CharField(max_length=250)),
                ('weight', models.FloatField()),
                ('layer', models.PositiveIntegerField()),
            ],
        ),
    ]
