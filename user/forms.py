from django import forms
from django.core.exceptions import ValidationError
from django.http import request

from user.manage import UserManager
from user.models import User, Post
from . import models
import datetime


class UserCreationForm(forms.ModelForm):
    first_name = forms.CharField(label='Enter First Name', max_length=150)
    last_name = forms.CharField(label='Enter Last Name', max_length=150)
    email = forms.EmailField(label='Enter email', max_length=50)
    username = forms.CharField(max_length=15)
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = models.User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user


class PostForm(forms.ModelForm):
    text = forms.CharField(label="Write Your Text Here", max_length=200, widget=forms.Textarea(attrs={'rows': 3}))

    class Meta:
        model = Post
        fields = ['text']
