# codding=utf-8
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .forms import *
from .models import *


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


class ArticleDescView(View):
    def get(self, request):
        article = ArticleModel.objects.get(id=int(request.GET.get('id')))
        return render(request, 'ArticleDesc.html', {'article': article})
