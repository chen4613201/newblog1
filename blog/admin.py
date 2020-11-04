from django.contrib import admin
from .models import *
# Register your models here.


class MenuModelAdmin(admin.ModelAdmin):
    list_display = ['mname', 'murl']


class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'desc', 'createtime', 'modifytime', 'catagory']


class TagModelAdmin(admin.ModelAdmin):
    list_display = ['tname']


class CatagoryModelAdmin(admin.ModelAdmin):
    list_display = ['cname']


admin.site.register(MenuModel, MenuModelAdmin)
admin.site.register(CatagoryModel, CatagoryModelAdmin)
admin.site.register(TagModel, TagModelAdmin)
admin.site.register(ArticleModel, ArticleModelAdmin)