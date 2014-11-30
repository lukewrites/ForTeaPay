from django import forms
from django.utils import timezone
from payreports.models import Employer


# class teacherForm(ModelForm):
#
#
#     class Meta:
#         model = Teacher
#         fields = (user_name, first_name, last_name, password, password_check, email)
#

class employerForm(forms.ModelForm):

    PROVINCE_LIST = (
        ('AH', 'Anhui'),
        ('BJ', 'Beijing'),
        ('CQ', 'Chongqing'),
        ('FJ', 'Fujian'),
        ('GS', 'Gansu'),
        ('GD', 'Guandong'),
        ('GX', 'Guangxi'),
        ('GZ', 'Guizhou'),
        ('HI', 'Hainan'),
        ('HE', 'Hebei'),
        ('HL', 'Heilongjiang'),
        ('HA', 'Henan'),
        ('HK', 'Hong Kong'),
        ('HB', 'Hubei'),
        ('HN', 'Hunan'),
        ('NM', 'Inner Mongolia'),
        ('JS', 'Jiangsu'),
        ('JX', 'Jiangxi'),
        ('JL', 'Jilin'),
        ('LN', 'Liaoning'),
        ('MC', 'Macao'),
        ('NX', 'Ningxia'),
        ('QH', 'Qinghai'),
        ('SN', 'Shaanxi'),
        ('SD', 'Shandong'),
        ('SH', 'Shanghai'),
        ('SX', 'Shanxi'),
        ('SC', 'Sichuan'),
        ('TW', 'Taiwan'),
        ('TJ', 'Tianjin'),
        ('XZ', 'Tibet'),
        ('XJ', 'Xinjiang'),
        ('YN', 'Yunnan'),
        ('ZJ', 'Zhejiang'),
    )

    GOOD = 'G'
    NEUTRAL = 'N'
    BAD = 'B'

    RATINGS = (
        (GOOD, 'Good'),
        (NEUTRAL, 'Neutral'),
        (BAD, 'Bad')
    )

    YES = 'Y'
    NO = 'N'
    MAYBE = 'M'

    RECOMMEND = (
        (YES, 'Yes'),
        (MAYBE, 'Maybe'),
        (NO, 'No')
    )

    YES_NO_CHOICES = (
        (YES, 'Yes'),
        (NO, 'No'),
    )

    FULL_TIME = 'FT'
    PART_TIME = 'PT'

    CONTRACT_TYPE_CHOICES = (
        (FULL_TIME, 'Full-time'),
        (PART_TIME, 'Part-time'),
    )

    HOURLY = 'H'
    MONTHLY = 'M'

    HOURLY_MONTHLY_CHOICES = (
        (HOURLY, 'Hourly'),
        (MONTHLY, 'Monthly'),
    )

    school_name = forms.CharField(required=True, max_length=128, help_text="Please enter the school's name.")
    school_city = forms.CharField(required=True, blank=False, max_length=20,
                                   help_text="Please enter the city in which the school was located.")
    school_province = forms.CharField(blank=False,
                                       max_length=2,
                                       choices=PROVINCE_LIST,
                                       help_text="Please select the school's province.")
    school_experience = forms.CharField(blank=False,
                                         max_length=7,
                                         choices=RATINGS,
                                         help_text="How would you rate your experience teaching at this school?",
                                         default=NEUTRAL)
    recommend_school = forms.CharField(blank=False,
                                    max_length=5,
                                    choices=RECOMMEND,
                                    help_text="Would you recommend this school to a friend?",
                                    default=MAYBE)
    date_report_added = forms.DateField(default=timezone.now())
    start_year = forms.IntegerField(blank=False,
                                 max_length=4,
                                 default=2014,
                                 help_text="In what year did this contract start?")
    end_year = forms.IntegerField(blank=False,
                               max_length=4,
                               default=2014,
                               help_text="In what year did/will the contract end?")

    class Meta:
        model = Employer
        fields = (school_name, school_city, school_province, school_experience, recommend_school, date_report_added,
                  start_year, end_year)
