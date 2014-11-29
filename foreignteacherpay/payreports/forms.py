from django.forms import ModelForm
from foreignteacherpay.payreports.models import Teacher, Employer


class teacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = [user_name, first_name, last_name, password, password_check, email]


class employerForm(ModelForm):
    class Meta:
        model = Employer
        fields = [school_name, school_city, school_province, school_experience, recommend_school]
