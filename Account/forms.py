from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import AuthenticationForm, AdminPasswordChangeForm
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMessage

from .models import User, UserManager


class UserCreationForm(forms.ModelForm):
    # 사용자 생성 폼
    email = forms.EmailField(
        label=_('Email'),
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Email address1'),
                'required': 'True',
            }
        )
    )
    name = forms.CharField(
        label=_('Name'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Name'),
                'required': 'True',
            }
        )
    )
    phone = forms.CharField(
        label=_('Phone'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Phone'),
                'required': 'True',
            }
        )
    )
    type = forms.CharField(
        label=_('Type'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Type'),
                'required': 'True',
            }
        )
    )
    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Password'),
                'required': 'True',
            }
        )
    )
    password2 = forms.CharField(
        label=_('Password confirmation'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Password confirmation'),
                'required': 'True',
            }
        )
    )

    class Meta:
        model = User
        fields = ('email', 'name','phone','type')

    def clean_password2(self):
        # 두 비밀번호 입력 일치 확인
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.email = UserManager.normalize_email(self.cleaned_data['email'])
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    # 관리 인터페이스에서 사용자의 정보와 권한을 변경하는 데 사용되는 양식.
    password = ReadOnlyPasswordHashField(
        label=_('Password')
    )

    class Meta:
        model = User
        fields = ('email', 'password','name','phone', 'type','is_active', 'is_superuser')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class PasswordChangeForm(AdminPasswordChangeForm):

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '  NEW PASSWORD',
                'required': 'True',
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '  NEW PASSWORD AGAIN',
                'required': 'True',
            }
        )
    )


class WebUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        # important to "pop" added kwarg before call to parent's constructor
#        self.request = kwargs.pop('request')
        super(UserCreationForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        user = super(WebUserCreationForm, self).save(commit=False)

        if commit:
            user.is_active = False
            user.save()

            # Send user activation mail
            #current_site = get_current_site(self.request)
            #subject = (_('Welcome To %s! Confirm Your Email') % current_site.name)
            subject = 'Welcome To Loka! Confirm Your Email'
            message = render_to_string('registration/user_activate_email.html', {
                'user': user,
           #     'domain': current_site.domain,
                'domain' : 'localhost:8000',
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': PasswordResetTokenGenerator().make_token(user),
            })
            email = EmailMessage(subject, message, to=[user.email])
            email.send()
        return user


''' terms = forms.BooleanField(
        label=_('Terms of service'),
        widget=forms.CheckboxInput(
            attrs={
                'required': 'True',
            }
        ),
        error_messages={
            'required': _('You must agree to the Terms of service to sign up'),
        }
    )
    privacy = forms.BooleanField(
        label=_('Privacy policy'),
        widget=forms.CheckboxInput(
            attrs={
                'required': 'True',
            }
        ),
        error_messages={
            'required': _('You must agree to the Privacy policy to sign up'),
        }
    )
'''

#login 폼
'''
class LoginForm(AuthenticationForm):
   email = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'email adress',
                'required': 'True',
            }
        )
    )


   password = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Password'),
                'required': 'True',
            }
        )
    )
    '''


   

