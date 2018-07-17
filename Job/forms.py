from django import forms
from .models import Job_info
from Account.models import User

FLIGHT_CHOICES = (
    ('None', 'None'),
    ('One-way', 'One-way'),
    ('Round-trip', 'Round-trip'),
)

AGE_CHOICES = (
    ('Kindergarten', 'Kindergarten'),
    ('Elementary', 'Elementary'),
    ('Middle', 'Middle'),
)


class Job_InfoForm(forms.Form):
    school_name = forms.CharField()
    start_date = forms.DateField()

    age_level = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=AGE_CHOICES,
    )
    location = forms.CharField()
    contract_period = forms.CharField()
    day_hour = forms.CharField()
    min_salary = forms.FloatField()
    max_salary = forms.FloatField()

    flight_support = forms.ChoiceField(
        widget=forms.Select,
        choices=FLIGHT_CHOICES,
    )
    house = forms.BooleanField(required=False)
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

    description = forms.CharField(
        widget=forms.Textarea(),
        required=False
    )

    qualification = forms.CharField(
        widget=forms.Textarea(),
        required=False
    )

    user = forms.CharField()

    # ModelForm.save 인터페이스를 흉내내어 구현
    def save(self, commit=True):
        post = Job_info(**self.cleaned_data)
        if commit:
            post.save()
        return post

