from django import forms
from captcha.fields import CaptchaField


class UserForm(forms.Form):
    account = forms.CharField(label="账号",max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码",max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码')

class RegisterForm(forms.Form):
    account = forms.CharField(
        label="账号",
        max_length=20,
        error_messages={
          "required":"账号不能为空",
        },
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    name = forms.CharField(
        label="姓名",
        max_length=128,
        error_messages={
            "required":"姓名不能为空"
        },
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    password1 = forms.CharField(
        label="密码",
        min_length=6,
        error_messages={
          "required":"密码不能为空"
        },
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="确认密码",
        max_length=256,
        error_messages={
            "required": "确认密码不能为空"
        },
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    phone = forms.CharField(
        label="手机号", max_length=256,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(label="邮箱地址",widget=forms.EmailInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码')
