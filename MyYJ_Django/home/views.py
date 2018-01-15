#!/usr/bin/env python
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect  # 重定向


# Create your views here.
def index(request):
    return render(request,'home.html')


def login(request):
    # f = open('templates/login.html', 'r', encoding='utf-8');
    # data = f.read()
    # f.close()
    # return HttpResponse(data)
    # 获取用户提交方法
    error_msg = ""
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        user = request.POST.get('user', None)
        pwd = request.POST.get('pwd', None)
        if user == 'root' and pwd == '123':
            # 跳转到主页
            return redirect("/index")  # 登录成功跳转到主页
        else:
            error_msg = "用户名/密码不匹配"

    return render(request, 'login.html', {'error_msg': error_msg})
