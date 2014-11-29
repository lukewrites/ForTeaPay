# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('payreports', '0007_auto_20141129_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='date_report_added',
            field=models.DateField(default=datetime.datetime(2014, 11, 29, 14, 4, 38, 786876, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
