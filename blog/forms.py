#coding=utf-8

from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db.models import Model


class LoginForm(forms.Form):
    login_user = forms.CharField(max_length=30, label=u'用户名:')
    login_pass = forms.CharField(max_length=30, widget=forms.PasswordInput, label=u'密  码:')


class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(max_length=30, label=u'确认密码:', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')
        print(model.username)

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            self.errors['password2'] = u'两次密码不一致'
        return data['password']
