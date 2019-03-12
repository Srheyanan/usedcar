# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-12 09:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sale', '0001_initial'),
        ('userinfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userinfo.UserInfo', verbose_name='用户'),
        ),
    ]
