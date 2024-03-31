from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from .models import Profile


User=get_user_model()

class UserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Firstname'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Lastname'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password1", "password2"]
        


class ProfileForm(ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Firstname'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Lastname'}))
    class Meta:
        model = Profile
        fields = ["username", "first_name", "last_name", "profile_picture"]