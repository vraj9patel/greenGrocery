from django import forms
from django.core import validators
from .models import UserProfileInfo, GuestEmail
from django.contrib.auth.models import User
from django.contrib.auth import password_validation


class GuestForm(forms.Form):
    email = forms.CharField(
        label="Email",
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        validators=[
            validators.RegexValidator(
                regex='^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$', message="Must be valid...")
        ]
    )


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        validators=[
            validators.RegexValidator(
                regex='^[A-Za-z]{3,30}$', message="Must be valid...")
        ]
    )
    password = forms.CharField(
        label="Password",
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )


class UserForm(forms.ModelForm):
    first_name = forms.CharField(
        label="First Name",
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        validators=[
            validators.RegexValidator(
                regex='^[A-Za-z]{3,30}$', message="Must be valid...")
        ]
    )
    last_name = forms.CharField(
        label="Last Name",
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        validators=[
            validators.RegexValidator(
                regex='^[A-Za-z]{3,30}$', message="Must be valid...")
        ]
    )
    email = forms.CharField(
        label="Email",
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        validators=[
            validators.RegexValidator(
                regex='^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$', message="Must be valid...")
        ]
    )

    username = forms.CharField(
        label="Username",
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        validators=[
            validators.RegexValidator(
                regex='^[A-Za-z]{3,30}$', message="Must be valid...")
        ]
    )

    password = forms.CharField(
        label="Password",
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    def clean_password(self):
        password = self.cleaned_data.get('password')
        try:
            password_validation.validate_password(password, self.instance)
        except forms.ValidationError as error:
            self.add_error('password', error)
        return password

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'password',
            'email'
        ]


class UserProfileInfoForm(forms.ModelForm):
    mobile = forms.CharField(
        label="Mobile Number",
        max_length=10,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'onkeypress': 'return onlyNumberKey(event)'
        }),
        validators=[
            validators.RegexValidator(
                regex='^[6-9]\d{9}$', message="Must be valid...")
        ]
    )

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')

        if UserProfileInfo.objects.filter(mobile=mobile):
            raise forms.ValidationError(
                'User with this mobile number already exists. Login to continue'
            )
        else:
            return mobile

    class Meta():
        model = UserProfileInfo
        fields = ['mobile']
