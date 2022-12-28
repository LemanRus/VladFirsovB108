from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.password_validation import validate_password
from django.utils.datetime_safe import datetime

from .models import CustomUser


class UserActions:
    birth_date = forms.DateField(label='Birth date', input_formats=['%d-%m-%Y'],
                                 widget=forms.SelectDateWidget(
                                     years=range(datetime.now().year - 70, datetime.now().year + 1), attrs={
                                         'class': 'form-control',
                                         'placeholder': 'dd-mm-yyyy',
                                     }))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('Enter email!')
        if email and CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Email entered is not free')
        return email


class SignupForm(UserCreationForm, UserActions):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'birth_date', 'photo', 'telephone', 'secret_question', 'secret_answer')


class PasswordResetValidateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, validators=[validate_password])

    class Meta:
        model = CustomUser
        fields = ('secret_answer', 'password')
        labels = {
            'secret_answer': 'Answer',
            'password': 'Enter your new password',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('Enter email!')
        if email and not CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Email doesn\'t exist. Please sign up')
        return email


class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email',
                  'birth_date', 'photo', 'telephone'
                  ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['birth_date'].widget.years = range(datetime.now().year - 70, datetime.now().year + 1)
