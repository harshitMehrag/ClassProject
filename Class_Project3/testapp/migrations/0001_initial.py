# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-06-08 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('ceo', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
            ],
        ),
    ]
