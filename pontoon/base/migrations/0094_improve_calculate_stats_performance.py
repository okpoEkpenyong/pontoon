# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-06 19:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0093_auto_20170517_2246'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='entity',
            index_together=set([('resource', 'obsolete', 'string_plural')]),
        ),
        migrations.AlterIndexTogether(
            name='translation',
            index_together=set([('entity', 'locale', 'approved'), ('entity', 'locale', 'fuzzy')]),
        ),
    ]