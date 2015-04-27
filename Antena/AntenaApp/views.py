# -*- coding: utf-8 -*-

from django.shortcuts import render

from form import NewsForm
from django.http import JsonResponse
from models import News
import json
from django.http import HttpResponse
from collections import OrderedDict

def top(request):
    form = NewsForm()
    return JsonResponse({'result': 'ok'})

def putNews(request,start=1,limit=30,search=None):
    try:
        start = request.GET['start']
        limit = request.GET['limit']
        search = request.GET['search']
    except:
        pass
    if search:
        news_list = News.objects.filter(title=search).filter(
                                        content=search)[start:start+limit]
    else:
        news_list = News.objects.all()[start:start+limit]

    # json_list = []
    # json_dict = {}
    news_dict_list = []

    for news in news_list:
        news_dict = OrderedDict([
            ("title", news.title),
            ("thumb_url", news.thumb_url)
        ])
        news_dict_list.append(news_dict)
        # json_dict.update({"title":news.title,"thumb_url":news.thumb_url})
        # json_list.append(json_dict)

    json_str = json.dumps(news_dict_list,ensure_ascii=False,indent=2)
    response = HttpResponse(json_str, content_type='application/json; charset=UTF-8',status=200)

    return response


