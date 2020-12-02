from django.conf.urls import url
from . import views
import os
app_name = 'OnlineTables'


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index')
]