#coding=utf-8

from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^index/$', views.IndexView.as_view(), name='index'),
    url(r'^catagory/(?P<catagory_id>\d+)/$', views.CatagoryView.as_view(), name='catagory'),
    url(r'^tag/(?P<tag_id>\d+)/$', views.TagView.as_view(), name='tag'),
    url(r'^ArticleDesc/$', views.ArticleDescView.as_view(), name='articledesc'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^register/$', views.RegisterView.as_view(), name='register')
]