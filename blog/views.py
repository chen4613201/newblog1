# codding=utf-8
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from .forms import *
from .models import *
from django.contrib import auth
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password

# Create your views here.


class IndexView(View):
    def get(self, request):
        # 获取分页参数Page
        current_page = request.GET.get('page', 1)
        # 获取当前分页参数的数据
        articles = ArticleModel.objects.all()
        paginator = Paginator(articles, 3)
        page_obj = paginator.get_page(current_page)
        return render(request, 'index.html', {'page_obj': page_obj})


class CatagoryView(View):
    def get(self, request, catagory_id):
        current_page = request.GET.get('page', 1)
        current_catagory = int(catagory_id)
        articles = ArticleModel.objects.filter(catagory__id=current_catagory)
        paginator = Paginator(articles, 3)
        page_obj = paginator.get_page(current_page)
        return render(request, 'catagory.html', {'page_obj': page_obj, 'catagory_id': catagory_id})


class TagView(View):
    def get(self, request, tag_id):
        current_page = request.GET.get('page', 1)
        tag_id = int(tag_id)
        articles = ArticleModel.objects.filter(tag__id=int(tag_id))
        paginator = Paginator(articles, 3)
        page_obj = paginator.get_page(current_page)
        return render(request, 'tag.html', {'page_obj': page_obj, 'tag_id': tag_id})


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        return render(request, 'login.html', {'login_form': login_form})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            data = login_form.cleaned_data
            user = auth.authenticate(username=data['login_user'], password=data['login_pass'])

            if user is not None:
                login(request, user)
                return HttpResponse('登录成功')
            else:
                return HttpResponse('用户名或密码错误,请重新输入')
        else:
            return HttpResponse('登录错误')


class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('/blog/index/')


class RegisterView(View):
    def get(self, request):

        register_form = UserCreationForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = UserCreationForm(request.POST)
        print(register_form.is_valid())
        if register_form.is_valid():
            data = register_form.cleaned_data
            username = data['username']
            password = register_form.clean_password2()
            print(username,password)
            try:
                user = User.objects.create(username=username, password=make_password(password))
            except Exception as e:
                print(e)
            print(user)
            if user is not None:
                return HttpResponse('注册成功')
        else:
            return HttpResponse('用户名或密码不符合安全规则')


class ArticleDescView(View):
    def get(self, request):
        article = ArticleModel.objects.get(id=int(request.GET.get('id')))
        return render(request, 'ArticleDesc.html', {'article': article})
