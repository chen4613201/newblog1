#coding=utf-8

from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^index/$', views.IndexView.as_view(), name='index'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^register/$', views.RegisterView.as_view(), name='register')
]