from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Kayıt olma ve giriş yapma formlarını django form altyapısı ile kurgulanıyor
class RegisterForm(UserCreationForm):
    first_name=forms.CharField(
        label = "Adı",
        widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Adı'
    }))
    last_name=forms.CharField(
        label = "Soyadı",
        widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Soyadı'
    }))
    username=forms.CharField(
        label = "Kullanıcı Adı",
        widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Kullanıcı Adı'
    }))
    email=forms.CharField(
        label = "Email",
        widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Email'
    }))
    password1=forms.CharField(
        label = "Şifre",
        widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Şifre'
    }))
    password2=forms.CharField(
        label = "Tekrar Şifre",
        widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Tekrar Şifre'
    }))
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']

class LoginForm(forms.Form):
    username=forms.CharField(
        label = "Kullanıcı Adı",
        widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Kullanıcı Adı'
    }))
    password=forms.CharField(
        label = "Şifre",
        widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Şifre'
    }))

