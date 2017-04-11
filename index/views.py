<<<<<<< HEAD
# -*- coding:utf-8 -*-
=======
# -*- coding: utf-8 -*-
>>>>>>> b5214b60a1b25e519f145c0653fb47aa98f1203b
from django.shortcuts import render
from django.shortcuts import redirect

# 认证的库
from django.contrib.auth import authenticate
from django.contrib.auth import login
# 登陆
from django.contrib.auth.models import User

from query.forms import DevRoomForm
from .forms import UserForm
from .forms import UserFormRegister

# Create your views here.


def index(request):
    """
    The index page of website
    """
    form = DevRoomForm()
    card1 = {'title': '开灯',
             'color': 'blue',
             'content': 'Turn on your light.',
             'action1': {'url': '/queryall/', 'name': '查询'},
             'action2': {'url': '/queryall/', 'name': '查询'}}
    card2 = {'title': '开灯',
             'color': 'green',
             'content': 'Turn on your light.',
             'action1': {'url': '/queryall/', 'name': '查询'},
             'action2': {'url': '/queryall/', 'name': ''}}
    cards = []
    cards.append(card1)
    cards.append(card2)
    formdata = {
        'title': '查询',
        'color': 'white',
        'url': '/queryall/',
        'content': 'Query all data from database.',
    }
    return render(request, 'index.html', {
        'form': form,
        'formData': formdata,
        'cards': cards})


def dorm_login(request):
    """
    The login page
    """
    form = UserForm()
    title = '登陆'
    url = '/login/'
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            # 获取表单信息
            username = user_form.cleaned_data['user_name']
            password = user_form.cleaned_data['user_password']
            # 认证
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return redirect(request, 'index.html',
                                {'title': username})
            else:
                # Return an 'invalid login' error message.
                error = '用户名或密码错误!'
                return render(request, 'login.html',
                              {'form': form,
                               'error': error,
                               'title': title,
                               'url': url})
        else:
            # 表单无效
            error = '请重试!'
            return render(request, 'login.html',
                          {'form': form,
                           'error': error,
                           'title': title,
                           'url': url})
    else:
        return render(request, 'login.html',
                      {'form': form,
                       'title': title,
                       'url': url})


def dorm_register(request):
    """
    The register page
    """
    form = UserFormRegister()
    title = '注册'
    url = '/register/'
    if request.method == "POST":
        user_form = UserFormRegister(request.POST)
        if user_form.is_valid():
            # 获取表单信息
            username = user_form.cleaned_data['user_name']
            password = user_form.cleaned_data['user_password']
            password_confirm = user_form.cleaned_data['user_password_confirm']
            if password == password_confirm:
                # 将表单写入数据库
                user = User.objects.create_user(
                    username=username, password=password)
                error = '成功'
                return render(request, 'login.html',
                              {'form': form,
                               'error': error,
                               'url': url})
            else:
                error = '两次密码不一致!'
                return render(request, 'login.html',
                              {'form': form,
                               'error': error,
                               'title': title,
                               'url': url})
        else:
            # 表单无效
            error = '请重试!'
            return render(request, 'login.html',
                          {'form': form,
                           'error': error,
                           'title': title,
                           'url': url})
    else:
        return render(request, 'login.html',
                      {'form': form,
                       'title': title,
                       'url': url})
