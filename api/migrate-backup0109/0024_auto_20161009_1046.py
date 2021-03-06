# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-09 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_auto_20161009_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='iapreceipthistory',
            name='bundle_id',
            field=models.CharField(blank=True, db_index=True, max_length=128, null=True, unique=True, verbose_name='iOS bundle_id'),
        ),
        migrations.AlterField(
            model_name='usergameorder',
            name='trade_id',
            field=models.CharField(db_index=True, max_length=32, null=True, unique=True, verbose_name='\u652f\u4ed8\u4e2d\u5fc3\u8ba2\u5355id'),
        ),
    ]
