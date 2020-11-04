from .models import *


def content_data(request):
    print('这是我定义的上下文')
    contents = {}
    #获取所有文章
    articles = ArticleModel.objects.all().order_by('catagory_id')
    #多对多关系中获取标签分类文章数量
    articles_by_tag = TagModel.objects.values('tname', count=Count('articlemodel'))
    #获取所有菜单
    menus = MenuModel.objects.all()

    #封装
    contents['articles'] = articles
    contents['articles_by_tag'] = articles_by_tag
    contents['menus'] = menus
    return {'contents': contents}
