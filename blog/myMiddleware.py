#coding=utf-8
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class testMiddleware(MiddlewareMixin):
    def process_request(self, request):
        path = request.path.lstrip("/")
        print(path)
