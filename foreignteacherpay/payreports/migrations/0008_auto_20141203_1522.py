# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('payreports', '0007_employer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='date_report_added',
            field=models.DateField(default=datetime.datetime(2014, 12, 3, 7, 22, 57, 956994, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='employer',
            name='teacher',
            field=models.ForeignKey(to='payreports.Teacher', blank=True),
            preserve_default=True,
        ),
    ]
