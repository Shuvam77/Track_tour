import email
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile


class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True,
        widget=forms.TextInput(attrs={'placeholder': '*Your First Name...'}))

    last_name = forms.CharField(max_length=30, required=True,
        widget=forms.TextInput(attrs={'placeholder': '*Your Last Name...'}))

    email = forms.EmailField(max_length=254, required=True,
        widget=forms.TextInput(attrs={'placeholder': '*Your Email Address...'}))

    password = forms.PasswordInput(max_length=30, required=True,
        widget=forms.TextInput(attrs={'placeholder': '*Your Password...', 'class':'password'}))

    password2 = forms.PasswordInput(max_length=30, required=True,
        widget=forms.TextInput(attrs={'placeholder': '*Confirm Password...', 'class':'password'}))


    #reCAPTCHA Token
    token = forms.CharField(
        widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = '__all__'

class AuthForm(AuthenticationForm):
    """
    FOrm that uses build-in AuthenticationForm to handel user auth
    """
    username  = forms.EmailField(max_length=254, required=True, widget = forms.TextInput(attrs={'placeholder': 'Email Address..'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '*Password..', 'class':'password'}))

    class Meta:
        model = User
        fields = ('username', 'password', )


class UserProfileForm(forms.ModelForm):
    """
    Basic model-form for our user profile that extends DJango user model.
    """
    address = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    town = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    county = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    post_code = forms.CharField(max_length=8, required=True, widget=forms.HiddenInput())
    country = forms.CharField(max_length=40, required=True, widget=forms.HiddenInput())
    longitude = forms.CharField(max_length=50, required=True, widget=forms.HiddenInput())
    latitude = forms.CharField(max_length=50, required=True, widget=forms.HiddenInput())

    class Meta:
        model = UserProfile
        fields = ('address', 'town', 'county', 'post_code', 'country', 'longitude', 'latitude')


    