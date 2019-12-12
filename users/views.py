from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
import json
from . import models
import hashlib
# Create your views here.


def registShow(request):

    return render(request, 'regist.html')


def loginShow(request):
    if request.session.get('user_id', default='') != '':
        return render(request, 'index.html')
    else:

        return render(request, 'login.html')


def regist(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data["username"]
        password = data["password"]
        isexist = models.user.objects.filter(username=username)
        # print(isexist)
        if len(isexist):
            context = {
                'status': 0,
                'message': '该用户名已经被注册'
            }
        else:
            sha1 = hashlib.sha1()
            sha1.update(password.encode())
            res1 = sha1.hexdigest()
            models.user.objects.create(username=username, password=res1)
            context = {
                'status': 1,
                'message': 'success'
            }
    return HttpResponse(json.dumps(context,ensure_ascii=False),content_type="application/json,charset=utf-8")


def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data["username"]
        password = data["password"]


        sha1 = hashlib.sha1()
        sha1.update(password.encode())
        res1 = sha1.hexdigest()
        isexist = models.user.objects.filter(username=username, password=res1)
        if len(isexist):
           request.session['user_id'] = username
           context = {
               'status': 1,
               'message': 'success'
           }
        else:
           context = {
               'status': 0,
               'message': '输入的账号或密码不正确'
           }

        return HttpResponse(json.dumps(context, ensure_ascii=False), content_type="application/json,charset=utf-8")


def logout(request):
    request.session.clear()  # 删除session里的全部内容
    return render(request, 'login.html')