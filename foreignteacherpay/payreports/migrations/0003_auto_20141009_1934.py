# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payreports', '0002_auto_20141009_1933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employer',
            name='recommend_school',
        ),
        migrations.RemoveField(
            model_name='employer',
            name='school_experience',
        ),
    ]
