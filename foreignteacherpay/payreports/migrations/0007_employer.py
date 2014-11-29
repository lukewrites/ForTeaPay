# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('payreports', '0006_auto_20141129_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school_name', models.CharField(help_text="Please enter the school's name.", max_length=100)),
                ('school_city', models.CharField(help_text='Please enter the city in which the school was located.', max_length=20)),
                ('school_province', models.CharField(max_length=2, help_text="Please select the school's province.", choices=[('AH', 'Anhui'), ('BJ', 'Beijing'), ('CQ', 'Chongqing'), ('FJ', 'Fujian'), ('GS', 'Gansu'), ('GD', 'Guandong'), ('GX', 'Guangxi'), ('GZ', 'Guizhou'), ('HI', 'Hainan'), ('HE', 'Hebei'), ('HL', 'Heilongjiang'), ('HA', 'Henan'), ('HK', 'Hong Kong'), ('HB', 'Hubei'), ('HN', 'Hunan'), ('NM', 'Inner Mongolia'), ('JS', 'Jiangsu'), ('JX', 'Jiangxi'), ('JL', 'Jilin'), ('LN', 'Liaoning'), ('MC', 'Macao'), ('NX', 'Ningxia'), ('QH', 'Qinghai'), ('SN', 'Shaanxi'), ('SD', 'Shandong'), ('SH', 'Shanghai'), ('SX', 'Shanxi'), ('SC', 'Sichuan'), ('TW', 'Taiwan'), ('TJ', 'Tianjin'), ('XZ', 'Tibet'), ('XJ', 'Xinjiang'), ('YN', 'Yunnan'), ('ZJ', 'Zhejiang')])),
                ('school_experience', models.CharField(max_length=7, default='N', choices=[('G', 'Good'), ('N', 'Neutral'), ('B', 'Bad')], help_text='How would you rate your experience teaching at this school?')),
                ('recommend_school', models.CharField(max_length=5, default='M', choices=[('Y', 'Yes'), ('M', 'Maybe'), ('N', 'No')], help_text='Would you recommend this school to a friend?')),
                ('date_report_added', models.DateField(default=datetime.datetime(2014, 11, 29, 14, 11, 17, 129052, tzinfo=utc))),
                ('start_year', models.IntegerField(default=2014, max_length=4, help_text='In what year did this contract start?')),
                ('end_year', models.IntegerField(default=2014, max_length=4, help_text='In what year did/will the contract end?')),
                ('contract_type', models.CharField(max_length=2, default='FT', choices=[('FT', 'Full-time'), ('PT', 'Part-time')], help_text='Full-time (FT) or Part-Time (PT) work.')),
                ('pay', models.IntegerField(blank=True, default=0, help_text='How much were you paid?')),
                ('type_of_wage', models.CharField(max_length=1, default='H', choices=[('H', 'Hourly'), ('M', 'Monthly')], help_text='Is the pay above hourly or monthly?')),
                ('hours_per_week', models.IntegerField(blank=True, default=0)),
                ('vacation_time', models.IntegerField(blank=True, default=0, max_length=3, help_text='Days of vacation per contract (EXCLUDING Chinese holidays).')),
                ('student_level', models.TextField(blank=True, help_text='What level(s) of students did you teach?')),
                ('housing', models.CharField(max_length=1, default='N', choices=[('Y', 'Yes'), ('N', 'No')], blank=True, help_text='Did the employer provide either a housing allowance or an apartment?')),
                ('housing_amount', models.IntegerField(blank=True, default=0, max_length=5, help_text='If money was provided for housing, how much?')),
                ('other_perks', models.CharField(blank=True, default='None.', max_length=500, help_text='Were there any other perks with the job? (Max 500 characters.)')),
                ('zed_visa', models.CharField(max_length=1, default='N', choices=[('Y', 'Yes'), ('N', 'No')], blank=True, help_text='Did the employer provide a Z visa & Residence Permit?')),
                ('your_comments', models.CharField(blank=True, default='None.', max_length=2000, help_text='Anything else to say about the job? (Max 2000 characters.)')),
                ('teacher', models.ForeignKey(to='payreports.Teacher')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
