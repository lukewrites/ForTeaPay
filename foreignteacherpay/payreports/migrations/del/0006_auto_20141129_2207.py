# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


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
            field=models.CharField(choices=[('FT', 'Full-time'), ('PT', 'Part-time')], help_text='Full-time (FT) or Part-Time (PT) work.', default='FT', max_length=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employer',
            name='date_report_added',
            field=models.DateField(default=datetime.datetime(2014, 11, 29, 14, 6, 51, 667920, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employer',
            name='end_year',
            field=models.IntegerField(help_text='In what year did/will the contract end?', default=2014, max_length=4),
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
            field=models.CharField(blank=True, help_text='Did the employer provide either a housing allowance or an apartment?', default='N', choices=[('Y', 'Yes'), ('N', 'No')], max_length=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employer',
            name='housing_amount',
            field=models.IntegerField(blank=True, help_text='If money was provided for housing, how much?', default=0, max_length=5),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employer',
            name='other_perks',
            field=models.CharField(blank=True, help_text='Were there any other perks with the job? (Max 500 characters.)', default='None.', max_length=500),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employer',
            name='pay',
            field=models.IntegerField(blank=True, help_text='How much were you paid?', default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employer',
            name='start_year',
            field=models.IntegerField(help_text='In what year did this contract start?', default=2014, max_length=4),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employer',
            name='student_level',
            field=models.TextField(blank=True, help_text='What level(s) of students did you teach?', default='NA'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employer',
            name='teacher',
            field=models.ForeignKey(default='luke', to='payreports.Teacher'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employer',
            name='type_of_wage',
            field=models.CharField(choices=[('H', 'Hourly'), ('M', 'Monthly')], help_text='Is the pay above hourly or monthly?', default='H', max_length=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employer',
            name='vacation_time',
            field=models.IntegerField(blank=True, help_text='Days of vacation per contract (EXCLUDING Chinese holidays).', default=0, max_length=3),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employer',
            name='your_comments',
            field=models.CharField(blank=True, help_text='Anything else to say about the job? (Max 2000 characters.)', default='None.', max_length=2000),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employer',
            name='zed_visa',
            field=models.CharField(blank=True, help_text='Did the employer provide a Z visa & Residence Permit?', default='N', choices=[('Y', 'Yes'), ('N', 'No')], max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='employer',
            name='recommend_school',
            field=models.CharField(choices=[('Y', 'Yes'), ('M', 'Maybe'), ('N', 'No')], help_text='Would you recommend this school to a friend?', default='M', max_length=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='employer',
            name='school_experience',
            field=models.CharField(choices=[('G', 'Good'), ('N', 'Neutral'), ('B', 'Bad')], help_text='How would you rate your experience teaching at this school?', default='N', max_length=7),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='user_name',
            field=models.CharField(unique=True, max_length=20),
            preserve_default=True,
        ),
    ]
