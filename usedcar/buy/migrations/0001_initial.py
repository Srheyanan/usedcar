# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-12 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=30, verbose_name='车辆信息')),
                ('picture', models.ImageField(default='normal.png', upload_to='', verbose_name='照片')),
                ('price', models.CharField(max_length=30, verbose_name='成交价格')),
                ('newprice', models.CharField(max_length=30, verbose_name='新车价格')),
                ('mileage', models.CharField(max_length=30, verbose_name='公里数')),
            ],
            options={
                'verbose_name_plural': '意愿表',
                'db_table': 'Cart',
                'verbose_name': '意愿表',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=30, verbose_name='车辆信息')),
                ('picture', models.ImageField(default='normal.png', upload_to='', verbose_name='照片')),
                ('price', models.CharField(max_length=30, verbose_name='成交价格')),
                ('newprice', models.CharField(max_length=30, verbose_name='新车价格')),
                ('mileage', models.CharField(max_length=30, verbose_name='公里数')),
                ('orderNo', models.CharField(max_length=30, verbose_name='订单号')),
                ('orderStatus', models.IntegerField(blank=True, choices=[(1, '未出价'), (2, '已出价'), (3, '订单关闭')], default='1', verbose_name='订单状态')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
            options={
                'verbose_name_plural': '订单表',
                'db_table': 'Orders',
                'verbose_name': '订单表',
            },
        ),
    ]
