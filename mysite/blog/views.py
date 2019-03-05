from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import *


def hello(request):
    return HttpResponse('欢迎使用Django！')



def index(request):
    allcategory = Category.objects.all()#通过Category表查出所有分类
    #把查询出来的分类封装到上下文里
    context = {
            'allcategory': allcategory,
        }
    return render(request, 'index.html', context)#把上下文传到index.html页面