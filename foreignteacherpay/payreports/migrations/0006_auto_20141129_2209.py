# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payreports', '0005_auto_20141010_1933'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employer',
        ),
        migrations.DeleteModel(
            name='JobReport',
        ),
        migrations.AlterField(
            model_name='teacher',
            name='user_name',
            field=models.CharField(unique=True, max_length=20),
            preserve_default=True,
        ),
    ]
