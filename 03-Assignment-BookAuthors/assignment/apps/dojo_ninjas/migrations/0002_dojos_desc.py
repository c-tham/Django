# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-21 00:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojos',
            name='desc',
            field=models.TextField(default='n/a'),
        ),
    ]
