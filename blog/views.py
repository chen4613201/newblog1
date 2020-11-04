from logging import Logger

from django.contrib.auth import authenticate
from django.core.handlers.asgi import logger
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.defaulttags import regroup
from django.views import View
from .forms import *
from django.contrib.auth.models import UserManager, User
from .models import *


# Create your views here.


class IndexView(View):
    def get(self, request):
        # 对文章分页显示
        articles = ArticleModel.objects.all()
        from django.core.paginator import Paginator
        paginator = Paginator(articles, 3)
        current_page = request.GET.get('PageNum')
        page_obj = paginator.get_page(current_page)
        print(request)
        print('会执行到这儿来吗')
        print(page_obj)
        return render(request, 'index.html', {'page_obj': page_obj })


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        return render(request, 'login.html', {'login_form': login_form})

    def post(self, request):
        data = request.Form
        return render(request, 'login.html')


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            data = register_form.cleaned_data
            user = User(username=data['username'], password=data['password'], email=data['email'])
            user.password = register_form.clean_password2()
            user.save()
            return HttpResponse('注册成功')
        return HttpResponse('注册失败')

