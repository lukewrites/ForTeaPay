# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('payreports', '0008_auto_20141129_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='date_report_added',
            field=models.DateField(default=datetime.datetime(2014, 11, 29, 14, 6, 0, 204517, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
