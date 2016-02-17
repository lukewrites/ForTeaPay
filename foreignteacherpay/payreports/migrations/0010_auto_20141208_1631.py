# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payreports', '0009_auto_20141203_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='date_report_added',
            field=models.DateField(default=b'2014-12-08'),
            preserve_default=True,
        ),
    ]
