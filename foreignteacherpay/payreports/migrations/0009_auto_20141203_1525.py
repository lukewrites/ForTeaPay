# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('payreports', '0008_auto_20141203_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employer',
            name='teacher',
        ),
        migrations.AlterField(
            model_name='employer',
            name='date_report_added',
            field=models.DateField(default=datetime.datetime(2014, 12, 3, 7, 25, 26, 512296, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
