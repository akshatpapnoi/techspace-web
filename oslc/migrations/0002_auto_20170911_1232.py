# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 12:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oslc', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Info',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]