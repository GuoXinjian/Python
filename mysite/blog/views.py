from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import *


def hello(request):
    return HttpResponse('欢迎使用Django！')



def index(request):
    allcategory = Category.objects.all()#通过Category表查出所有分类
    banner = Banner.objects.filter(is_active=True)[0:4]#查询所有幻灯图数据，并进行切片
    recommend = Article.objects.filter(recommend__id=1)[:3]#查询推荐位ID为1的文章
    allarticle = Article.objects.all().order_by('-id')[0:10]
    #hot = Article.objects.all().order_by('?')[:10]#随机推荐
    #hot = Article.objects.filter(recommend__id=3)[:10]   #通过推荐进行查询，以推荐ID是3为例
    hot = Article.objects.all().order_by('views')[:10]#通过浏览数进行排序
    remen = Article.objects.filter(recommend__id=2)[:6]
    tags = Tag.objects.all()
    link = Link.objects.all()
    #把查询出来的分类封装到上下文里
    context = {
            'allcategory': allcategory,
            'banner':banner, #把查询到的幻灯图数据封装到上下文
            'recommend':recommend,
            'allarticle': allarticle,
            'hot':hot,
            'remen':remen,
            'tags':tags,
            'link':link,
        }
    return render(request, 'index.html', context)#把上下文传到index.html页面

#首页
# def index(request):
#     pass

#列表页
def list(request,lid):
    pass

#内容页
def show(request,sid):
    pass

#标签页
def tag(request, tag):
    pass

# 搜索页
def search(request):
    pass
# 关于我们
def about(request):
    pass