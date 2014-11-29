# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payreports', '0004_auto_20141009_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobreport',
            name='pay',
            field=models.IntegerField(help_text='How much were you paid?'),
        ),
        migrations.AlterField(
            model_name='jobreport',
            name='vacation_time',
            field=models.IntegerField(help_text='Days of vacation per contract (EXCLUDING Chinese holidays).', max_length=3),
        ),
    ]
