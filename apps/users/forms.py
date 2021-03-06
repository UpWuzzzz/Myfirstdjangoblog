__author__ = 'awu'
__date__ = '2018/5/8 13:02'

from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={'invalid': '验证码输入错误'})


class RegisterForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
    email = forms.EmailField(required=True)
    sex = forms.CharField(required=True)
    captcha = CaptchaField(error_messages={'invalid': '验证码输入错误'})


class ForgetForm(forms.Form):
    username = forms.CharField(required=True)
    captcha = CaptchaField(error_messages={'invalid': '验证码输入错误'})


class ChangepsdForm(forms.Form):
    old_password = forms.CharField(required=True)
    password1 = forms.CharField(required=True)
    password2 = forms.CharField(required=True)