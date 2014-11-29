# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payreports', '0003_auto_20141009_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='recommend_school',
            field=models.CharField(choices=[('Yes', 'Yes'), ('Maybe', 'Maybe'), ('No', 'No')], default='Yes', max_length=5, help_text='Would you recommend this school to a friend?'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employer',
            name='school_experience',
            field=models.CharField(choices=[('Good', 'Good'), ('Neutral', 'Neutral'), ('Bad', 'Bad')], default='Good', max_length=7, help_text='How would you rate your experience teaching at this school?'),
            preserve_default=True,
        ),
    ]
