from django import forms
from .models import Job_info

FLIGHT_CHOICES = (
    ('none', 'none'),
    ('one-way', 'one-way'),
    ('round-trip', 'round-trip'),
)

AGE_CHOICES = (
    ('Kidergarten', 'Kindergarten'),
    ('Elementary', 'Elementary'),
    ('Middle', 'Middle'),
)


class Job_InfoForm(forms.Form):
    school_name = forms.CharField()
    start_date = forms.DateField(
        widget=forms.DateTimeInput()
    )

    age_level = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=AGE_CHOICES,
    )
    location = forms.CharField()
    contract_period = forms.CharField()
    day_hour = forms.CharField()
    min_salary = forms.FloatField()
    max_salary = forms.FloatField()

    flight_support = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=FLIGHT_CHOICES,
    )
    house = forms.BooleanField()
    house_pic = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={
                'multiple': True
            }
        )
    )
    severance_payment = forms.BooleanField()
    health_insurance = forms.BooleanField()
    national_pension = forms.BooleanField()

    # ModelForm.save 인터페이스를 흉내내어 구현
    def save(self, commit=True):
        post = Job_info(**self.cleaned_data)
        if commit:
            post.save()
        return post

