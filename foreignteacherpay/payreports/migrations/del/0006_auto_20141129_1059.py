# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('payreports', '0005_auto_20141010_1933'),
    ]

    operations = [
        migrations.DeleteModel(
            name='JobReport',
        ),
        migrations.AddField(
            model_name='employer',
            name='contract_type',
            field=models.CharField(choices=[('FT', 'Full-time'), ('PT', 'Part-time')], default='FT', help_text='Full-time (FT) or Part-Time (PT) work.', max_length=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employer',
            name='date_report_added',
            field=models.DateTimeField(blank=False, default=timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employer',
            name='end_year',
            field=models.IntegerField(default=2014, help_text='In what year did/will the contract end?', max_length=4),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employer',
            name='hours_per_week',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employer',
            name='housing',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], blank=True, default='N', help_text='Did the employer provide either a housing allowance or an apartment?', max_length=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employer',
            name='housing_amount',
            field=models.IntegerField(default=0, help_text='If money was provided for housing, how much?', max_length=5),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employer',
            name='other_perks',
            field=models.CharField(blank=True, default='None.', help_text='Were there any other perks with the job? (Max 500 characters.)', max_length=500),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employer',
            name='pay',
            field=models.IntegerField(blank=True, default=0, help_text='How much were you paid?'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employer',
            name='start_year',
            field=models.IntegerField(default=2014, help_text='In what year did this contract start?', max_length=4),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employer',
            name='student_level',
            field=models.TextField(blank=True, default='NA', help_text='What level(s) of students did you teach?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employer',
            name='teacher',
            field=models.ForeignKey(to='payreports.Teacher', default='None'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employer',
            name='type_of_wage',
            field=models.CharField(choices=[('H', 'Hourly'), ('M', 'Monthly')], default='H', help_text='Is the pay above hourly or monthly?', max_length=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employer',
            name='vacation_time',
            field=models.IntegerField(blank=True, default=0, help_text='Days of vacation per contract (EXCLUDING Chinese holidays).', max_length=3),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employer',
            name='your_comments',
            field=models.CharField(blank=True, default='None.', help_text='Anything else to say about the job? (Max 2000 characters.)', max_length=2000),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employer',
            name='zed_visa',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], blank=True, default='N', help_text='Did the employer provide a Z visa & Residence Permit?', max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='employer',
            name='recommend_school',
            field=models.CharField(choices=[('Y', 'Yes'), ('M', 'Maybe'), ('N', 'No')], default='M', help_text='Would you recommend this school to a friend?', max_length=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='employer',
            name='school_experience',
            field=models.CharField(choices=[('G', 'Good'), ('N', 'Neutral'), ('B', 'Bad')], default='N', help_text='How would you rate your experience teaching at this school?', max_length=7),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='user_name',
            field=models.CharField(unique=True, max_length=20),
            preserve_default=True,
        ),
    ]
