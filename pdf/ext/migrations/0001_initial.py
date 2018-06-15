# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-09 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pdf',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('author', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=200)),
                ('keywords', models.CharField(max_length=2000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('Creator', models.CharField(max_length=200)),
                ('Producer', models.CharField(max_length=200)),
            ],
        ),
    ]
