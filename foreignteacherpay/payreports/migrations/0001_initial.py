# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('school_name', models.CharField(max_length=100, help_text="Please enter the school's name.")),
                ('school_city', models.CharField(max_length=20, help_text='Please enter the city name.')),
                ('school_province', models.CharField(max_length=2, help_text='Please select the province.', choices=[('AH', 'Anhui'), ('BJ', 'Beijing'), ('CQ', 'Chongqing'), ('FJ', 'Fujian'), ('GS', 'Gansu'), ('GD', 'Guandong'), ('GX', 'Guangxi'), ('GZ', 'Guizhou'), ('HI', 'Hainan'), ('HE', 'Hebei'), ('HL', 'Heilongjiang'), ('HA', 'Henan'), ('HK', 'Hong Kong'), ('HB', 'Hubei'), ('HN', 'Hunan'), ('NM', 'Inner Mongolia'), ('JS', 'Jiangsu'), ('JX', 'Jiangxi'), ('JL', 'Jilin'), ('LN', 'Liaoning'), ('MC', 'Macao'), ('NX', 'Ningxia'), ('QH', 'Qinghai'), ('SN', 'Shaanxi'), ('SD', 'Shandong'), ('SH', 'Shanghai'), ('SX', 'Shanxi'), ('SC', 'Sichuan'), ('TW', 'Taiwan'), ('TJ', 'Tianjin'), ('XZ', 'Tibet'), ('XJ', 'Xinjiang'), ('YN', 'Yunnan'), ('ZJ', 'Zhejiang')])),
                ('school_experience', models.CharField(default='Good', max_length=7, help_text='How would you rate your experience teaching at this school?', choices=[('Good', 'Good'), ('Neutral', 'Neutral'), ('Bad', 'Bad')])),
                ('recommend_school', models.CharField(default='Yes', max_length=5, help_text='Would you recommend this school to a friend?', choices=[('Yes', 'Yes'), ('Maybe', 'Maybe'), ('No', 'No')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JobReport',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date_report_added', models.DateField(auto_now=True)),
                ('start_year', models.DateField(help_text='In what year did this contract start?')),
                ('end_year', models.DateField(help_text='In what year did/will the contract end?')),
                ('contract_type', models.CharField(default='FT', max_length=2, help_text='Full-time (FT) or Part-Time (PT) work.', choices=[('FT', 'Full-time'), ('PT', 'Part-time')])),
                ('pay', models.IntegerField(help_text='How much were you paid? Hourly or monthly')),
                ('type_of_wage', models.CharField(default='H', max_length=1, help_text='Is the pay above hourly or monthly?', choices=[('H', 'Hourly'), ('M', 'Monthly')])),
                ('hours_per_week', models.IntegerField()),
                ('vacation_time', models.IntegerField(max_length=3, help_text='Days of vacation per contract.')),
                ('year', models.IntegerField(max_length=4, help_text='Please enter the four digit year (e.g. 2008).')),
                ('student_level', models.TextField(help_text='What level(s) of students did you teach?')),
                ('housing', models.CharField(default='N', max_length=1, help_text='Did the employer provide either a housing allowance or an apartment?', choices=[('Y', 'Yes'), ('N', 'No')])),
                ('housing_amount', models.IntegerField(max_length=5, help_text='If money was provided for housing, how much?')),
                ('other_perks', models.TextField(max_length=500, help_text='Were there any other perks with the job? (Max 500 characters.)')),
                ('zed_visa', models.TextField(help_text='Did the employer provide a Z visa & Residence Permit?')),
                ('your_comments', models.TextField(max_length=2000, help_text='Anything else to say about the job? (Max 2000 characters.)')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('user_name', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=40)),
                ('password_check', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=75, unique=True)),
                ('confirmed', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
