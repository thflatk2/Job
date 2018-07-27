from django import forms
from .models import Job_info
from Account.models import User

FLIGHT_CHOICES = (
    ('None', 'None'),
    ('One-way', 'One-way'),
    ('Round-trip', 'Round-trip'),
)

class Job_InfoForm(forms.Form):
    job_title = forms.CharField()
    school_name = forms.CharField()
    class_size = forms.IntegerField(min_value=0)
    start_date = forms.DateField()
    age_level = forms.CharField()
    location = forms.CharField()
    contract_period = forms.CharField()
    day_hour = forms.CharField()
    min_salary = forms.FloatField(min_value=0.0)
    max_salary = forms.FloatField(min_value=0.0)

    flight_support = forms.ChoiceField(
        widget=forms.Select,
        choices=FLIGHT_CHOICES,
    )
    house = forms.BooleanField(required=False)
    allowance = forms.BooleanField(required=False)
    house_pic1 = forms.FileField(
        widget=forms.ClearableFileInput(),
        required=False
    )
    house_pic2 = forms.FileField(
        widget=forms.ClearableFileInput(),
        required=False
    )
    house_pic3 = forms.FileField(
        widget=forms.ClearableFileInput(),
        required=False
    )
    house_pic4 = forms.FileField(
        widget=forms.ClearableFileInput(),
        required=False
    )
    house_pic5 = forms.FileField(
        widget=forms.ClearableFileInput(),
        required=False
    )
    severance_payment = forms.BooleanField(required=False)
    health_insurance = forms.BooleanField(required=False)
    national_pension = forms.BooleanField(required=False)

    summary = forms.CharField(
        widget=forms.TextInput(),
        required=True
    )

    user = forms.CharField()

    # ModelForm.save 인터페이스를 흉내내어 구현
    def save(self, commit=True):
        post = Job_info(**self.cleaned_data)
        if commit:
            post.save()
        return post

