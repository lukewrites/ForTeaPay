# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payreports', '0005_auto_20141010_1933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employer',
            name='teacher',
        ),
        migrations.DeleteModel(
            name='Employer',
        ),
    ]
