from django.db import models
from django.utils import timezone



class Teacher(models.Model):
    user_name = models.CharField(max_length=20, blank=False, unique=True)
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    password = models.CharField(max_length=40, blank=False)
    password_check = models.CharField(max_length=40, blank=False)
    email = models.EmailField(blank=False, unique=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):  # __unicode__ on Python 2
        return self.first_name


class Employer(models.Model):

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

    teacher = models.ForeignKey("Teacher")
    school_name = models.CharField(blank=False,
                                   max_length=100,
                                   help_text="Please enter the school's name.")
    school_city = models.CharField(blank=False,
                                   max_length=20,
                                   help_text="Please enter the city in which the school was located.")
    school_province = models.CharField(blank=False,
                                       max_length=2,
                                       choices=PROVINCE_LIST,
                                       help_text="Please select the school's province.")
    school_experience = models.CharField(blank=False,
                                         max_length=7,
                                         choices=RATINGS,
                                         help_text="How would you rate your experience teaching at this school?",
                                         default=NEUTRAL)
    recommend_school = models.CharField(blank=False,
                                        max_length=5,
                                        choices=RECOMMEND,
                                        help_text="Would you recommend this school to a friend?",
                                        default=MAYBE)
    date_report_added = models.DateField(default=timezone.now())
    start_year = models.IntegerField(blank=False,
                                     max_length=4,
                                     default=2014,
                                     help_text="In what year did this contract start?")
    end_year = models.IntegerField(blank=False,
                                   max_length=4,
                                   default=2014,
                                   help_text="In what year did/will the contract end?")
    contract_type = models.CharField(blank=False,
                                     max_length=2,
                                     help_text="Full-time (FT) or Part-Time (PT) work.",
                                     choices=CONTRACT_TYPE_CHOICES,
                                     default=FULL_TIME)
    pay = models.IntegerField(blank=True,
                              default=0,
                              help_text="How much were you paid?")
    type_of_wage = models.CharField(help_text="Is the pay above hourly or monthly?",
                                    choices=HOURLY_MONTHLY_CHOICES,
                                    default=HOURLY,
                                    max_length=1)
    hours_per_week = models.IntegerField(blank=True,
                                         default=0)
    vacation_time = models.IntegerField(blank=True,
                                        default=0,
                                        help_text="Days of vacation per contract (EXCLUDING Chinese holidays).",
                                        max_length=3)
    student_level = models.TextField(blank=True,
                                     help_text="What level(s) of students did you teach?")
    housing = models.CharField(blank=True,
                               choices=YES_NO_CHOICES,
                               default=NO,
                               max_length=1,
                               help_text="Did the employer provide either a housing allowance or an apartment?")
    housing_amount = models.IntegerField(max_length=5,
                                         default=0,
                                         help_text="If money was provided for housing, how much?",
                                         blank=True,)
    other_perks = models.CharField(help_text="Were there any other perks with the job? (Max 500 characters.)",
                                   max_length=500,
                                   default='None.',
                                   blank=True)
    zed_visa = models.CharField(blank=True,
                                choices=YES_NO_CHOICES,
                                default=NO,
                                max_length=1,
                                help_text="Did the employer provide a Z visa & Residence Permit?")
    your_comments = models.CharField(max_length=2000,
                                     blank=True,
                                     default='None.',
                                     help_text="Anything else to say about the job? (Max 2000 characters.)")