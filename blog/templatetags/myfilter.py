#coding=utf-8
from django.template import Library

register = Library()


@register.filter
def md(value):
    import markdown
    print('我到了过滤器里面')
    print(markdown.markdown(value))
    return markdown.markdown(value)
