# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 20:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171122_1955'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Kategorija',
            new_name='category',
        ),
    ]
