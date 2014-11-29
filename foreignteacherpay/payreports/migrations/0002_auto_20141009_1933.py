# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payreports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='school_city',
            field=models.CharField(max_length=20, help_text='Please enter the city in which the school was located.'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='school_province',
            field=models.CharField(help_text="Please select the school's province.", choices=[('AH', 'Anhui'), ('BJ', 'Beijing'), ('CQ', 'Chongqing'), ('FJ', 'Fujian'), ('GS', 'Gansu'), ('GD', 'Guandong'), ('GX', 'Guangxi'), ('GZ', 'Guizhou'), ('HI', 'Hainan'), ('HE', 'Hebei'), ('HL', 'Heilongjiang'), ('HA', 'Henan'), ('HK', 'Hong Kong'), ('HB', 'Hubei'), ('HN', 'Hunan'), ('NM', 'Inner Mongolia'), ('JS', 'Jiangsu'), ('JX', 'Jiangxi'), ('JL', 'Jilin'), ('LN', 'Liaoning'), ('MC', 'Macao'), ('NX', 'Ningxia'), ('QH', 'Qinghai'), ('SN', 'Shaanxi'), ('SD', 'Shandong'), ('SH', 'Shanghai'), ('SX', 'Shanxi'), ('SC', 'Sichuan'), ('TW', 'Taiwan'), ('TJ', 'Tianjin'), ('XZ', 'Tibet'), ('XJ', 'Xinjiang'), ('YN', 'Yunnan'), ('ZJ', 'Zhejiang')], max_length=2),
        ),
    ]
