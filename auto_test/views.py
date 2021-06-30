from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from . import models
from .forms import UserForm,RegisterForm
import hashlib
import json



def index(request):
    return render(request, "index.html")

def register(request):
    if request.session.get('is_login',None):
        return redirect('/index/')
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            account = register_form.cleaned_data['account']
            name = register_form.cleaned_data['name']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            phone = register_form.cleaned_data['phone']
            email = register_form.cleaned_data['email']
            if password1 != password2:
                message = '两次密码输入不一致！'
                return render(request,'register.html',locals())
            same_account_user = models.User.objects.filter(account=account)
            if same_account_user:
                message = "账号已存在，请重新输入！"
                return render(request,'register.html')
            same_phone_user = models.User.objects.filter(phone=phone)
            if same_phone_user:
                message = "手机号已存在，请重新输入！"
                return render(request,'register.html')
            new_user = models.User.objects.create()
            new_user.account = account
            new_user.name = name
            new_user.password = hash_code(password1)
            new_user.phone = phone
            new_user.email = email
            new_user.save()
            return redirect('/login/')
    register_form = RegisterForm()
    return render(request,'register.html',locals())

def login(request):
    if request.session.get('is_login',None):
        return redirect('/index/')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "表单校验不通过，请检查输入值！"
        if login_form.is_valid():
            account = login_form.cleaned_data['account']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(account=account)
                if user.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['name'] = user.name
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！"
        return render(request,'login.html',locals())

    login_form = UserForm()
    return render(request,'login.html',locals())

def hash_code(s,salt='mysite_login'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()

def logout(request):
    if not request.session.get('is_login',None):
        return redirect('/index/')
    request.session.flush()
    return redirect('/index/')

def userList(request):
    users = models.User.objects.all()
    for i in users:
        print(i.id)
    return render(request,'userList.html',{'list':users})

def editUser(request):
    pass


def deleteUser(request):
    id = request.GET.get("id")
    models.User.objects.filter(id=id).delete()
    return redirect('/userList/')










