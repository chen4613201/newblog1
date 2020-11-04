from django.db import models
from django.db.models import Count


class MenuModel(models.Model):
    mname = models.CharField(max_length=10, unique=True, default=u'未定义', verbose_name='菜单名')
    murl = models.CharField(max_length=100)

    class Meta:
        db_table = 't_menu'
        verbose_name_plural = '菜单'


class TagModel(models.Model):
    tname = models.CharField(max_length=30, default=u'未定义', unique=True, verbose_name='标签名称')

    class Meta:
        db_table = 't_tag'
        verbose_name_plural = '标签'

    def __str__(self):
        return 'Tag:%s' % self.tname


class CatagoryModel(models.Model):
    cname = models.CharField(max_length=30,default=u'未定义', unique=True, verbose_name='分类名称')

    class Meta:
        db_table = 't_catagory'
        verbose_name_plural = '分类'

    def __str__(self):
        return u'Catagory:%s' % self.cname


class ArticleModel(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='文章标题')
    desc = models.CharField(max_length=300, verbose_name='描述')
    content = models.TextField(verbose_name='内容')
    createtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modifytime = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    tag = models.ManyToManyField(TagModel, verbose_name='标签')
    catagory = models.ForeignKey(CatagoryModel, on_delete=models.CASCADE, verbose_name='分类')

    class Meta:
        db_table = 't_article'
        verbose_name_plural = '文章'

    def __str__(self):
        return 'Article:%s' % self.title
