# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-10 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20161010_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iapreceipthistory2',
            name='iap_digest',
            field=models.CharField(max_length=255, unique=True, verbose_name='\u82f9\u679c\u652f\u4ed8\u9a8c\u8bc1\u4e32\u7684md5\u503c'),
        ),
    ]