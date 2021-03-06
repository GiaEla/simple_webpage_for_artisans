# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 19:55
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Kategorija', 'verbose_name_plural': 'Kategorije'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Objava', 'verbose_name_plural': 'Objave'},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='Kategorija',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='tags',
            new_name='Tagi',
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(max_length=350, verbose_name='Opis'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Ime'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Vsebina'),
        ),
        migrations.AlterField(
            model_name='post',
            name='lead',
            field=ckeditor.fields.RichTextField(verbose_name='Lead'),
        ),
        migrations.AlterField(
            model_name='post',
            name='sub_title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Podnaslov'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Naslov'),
        ),
    ]
