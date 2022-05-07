from django.shortcuts import render
from app.models import *
from django.views import View
from django.http.response import JsonResponse
from django.core import serializers
import json
from django.http import HttpResponseRedirect
def index(request):

    return HttpResponseRedirect('/static/index.html')  # 跳转到index界面

# Create your views here.
def list(request):
    # 取出五条数据,并序列化为json字符串
    article = serializers.serialize('json', Locations.objects.all())
    # 将字符串转换为json对象
    jsondata = json.loads(article)
    # 将data放入字典中
    data = {
        'data': jsondata,
        'code': '200',
        'message': '获取成功!'
    }
    return JsonResponse(data=data, safe=False)

def getEventsByLocation(request):
    requestLoaction = request.GET.get("location")
    locations = Locations.objects.get(locations=requestLoaction)
    events = locations.events_set.all()
    # 取出五条数据,并序列化为json字符串
    article = serializers.serialize('json',events)
    # 将字符串转换为json对象
    jsondata = json.loads(article)
    # 将data放入字典中
    data = {
        'data': jsondata,
        'code': '200',
        'message': '获取成功!'
    }
    return JsonResponse(data=data, safe=False)


def getFiguresByEvents(request):
    id = request.GET.get("id")
    events = Events.objects.get(id = id)
    figures = events.figures.all()
    # 取出五条数据,并序列化为json字符串
    article = serializers.serialize('json',figures)
    # 将字符串转换为json对象
    jsondata = json.loads(article)
    # 将data放入字典中
    data = {
        'data': jsondata,
        'code': '200',
        'message': '获取成功!'
    }
    return JsonResponse(data=data, safe=False)
def getEmotionsByFigures(request):
    id = request.GET.get("id")
    events = Events.objects.get(id = id)
    # 取出五条数据,并序列化为json字符串
    article = serializers.serialize('json',events.emotions.all())
    # 将字符串转换为json对象
    jsondata = json.loads(article)
    # 将data放入字典中
    data = {
        'data': jsondata,
        'code': '200',
        'message': '获取成功!'
    }
    return JsonResponse(data=data, safe=False)