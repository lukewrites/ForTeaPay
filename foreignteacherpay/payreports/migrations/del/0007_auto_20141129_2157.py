# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payreports', '0006_auto_20141129_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='date_report_added',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='employer',
            name='housing_amount',
            field=models.IntegerField(help_text='If money was provided for housing, how much?', blank=True, max_length=5, default=0),
            preserve_default=True,
        ),
    ]
