# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 21:11
from __future__ import unicode_literals

import borrow.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=borrow.models.get_image_path)),
                ('name', models.CharField(max_length=40)),
                ('is_borrowed', models.BooleanField(default=False)),
                ('tire_radius', models.FloatField(default=8)),
                ('threshold', models.FloatField(default=10)),
                ('description', models.CharField(max_length=400)),
                ('cost', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
