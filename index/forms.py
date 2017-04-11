# -*- coding:utf-8 -*-

from django import forms


class UserForm(forms.Form):
    """
    User and password form
    register
    """
    user_name = forms.CharField(label='用户名', max_length=100)
    user_password = forms.CharField(label='密码', widget=forms.PasswordInput())


class UserFormRegister(forms.Form):
    """
    User and password form
    register
    """
    user_name = forms.CharField(label='用户名', max_length=100)
    user_password = forms.CharField(label='密码', widget=forms.PasswordInput())
    user_password_confirm = forms.CharField(
        label='确认密码', widget=forms.PasswordInput())
