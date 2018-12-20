from django.shortcuts import render,redirect
from . import models
# Create your views here.

def index(request):
    pass
    return render(request,'login/index.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        message = "所有字段必须填写"
        if username and password:
            username = username.strip()
            #用户名字符合法性验证
            #密码长度验证
            #其他验证
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    print(username,password)
                    return redirect('/index/')
                else:
                    message="密码错误"
            except:
                message = '用户不存在'
        return render(request,'login/login.html',{'message':message})
            
    return render(request,'login/login.html')

def register(request):
    pass
    return render(request,'login/register.html')

def logout(request):
    pass
    return render('index/')