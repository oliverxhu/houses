# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-19 03:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adjacent_Suburbs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_suburb_adjacent', models.IntegerField()),
                ('last_updated', models.DateTimeField()),
                ('id_suburb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analytics.Suburb')),
            ],
        ),
        migrations.RemoveField(
            model_name='adjacent_suburb',
            name='id_adjacent_suburb',
        ),
        migrations.RemoveField(
            model_name='adjacent_suburb',
            name='id_listing',
        ),
        migrations.DeleteModel(
            name='Adjacent_Suburb',
        ),
    ]
