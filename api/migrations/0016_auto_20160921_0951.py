# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-21 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_app_pay_callback_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.SmallIntegerField(choices=[(0, '\u6b63\u5e38'), (1, '\u5c01\u53f7')], db_index=True, default=0, verbose_name='\u7528\u6237\u72b6\u6001'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, db_index=True, max_length=128, null=True, verbose_name='User Phone Number'),
        ),
    ]