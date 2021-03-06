# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-09 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_auto_20161004_0824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='package_name',
        ),
        migrations.AddField(
            model_name='app',
            name='package_names',
            field=models.TextField(blank=True, null=True, verbose_name='\u5305\u540d(bundle id)\u5217\u8868\uff0c\u7528\u82f1\u6587\u9017\u53f7\u9694\u5f00'),
        ),
        migrations.AddField(
            model_name='usergameorder',
            name='currency',
            field=models.CharField(default='cny', max_length=16, verbose_name='\u8ba2\u5355\u5bf9\u5e94\u7684\u8d27\u5e01\u5355\u4f4d'),
        ),
        migrations.AddField(
            model_name='usergameorder',
            name='real_amount',
            field=models.IntegerField(default=0, verbose_name='\u771f\u5b9e\u652f\u4ed8\u91d1\u989d\uff0c\u5355\u4f4d(\u5206)'),
        ),
        migrations.AlterField(
            model_name='usergameorder',
            name='amount',
            field=models.IntegerField(verbose_name='\u652f\u4ed8\u91d1\u989d\uff0c\u5355\u4f4d(\u5206)'),
        ),
    ]
