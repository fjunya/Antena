# -*- coding: utf-8 -*-

from django.shortcuts import render

from form import NewsForm
from django.http import JsonResponse
from models import News
import json
from django.http import HttpResponse
from collections import OrderedDict
from django.db.models import Q

def top(request):
    form = NewsForm()
    return JsonResponse({'result': 'ok'})

def putNews(request):
    try:
        start = int(request.GET['start'])
    except:
        start = 0
    try:
        limit = int(request.GET['limit'])
        limit += start
    except:
        limit = 30 + start
    try:
        search = request.GET['search']
    except:
        search = None

    if search:
        # search_news_list = News.objects.filter(title__icontains=search).filter(
        #                                 content__icontains=search)
        search_news_list = News.objects.filter(Q(title__icontains=search) |
                                               Q(content__icontains=search) |
                                               Q(sub_content__icontains=search))
        if search_news_list.count() > limit - start:
            news_list = search_news_list[start:limit]
        else:
            news_list = search_news_list
    else:
        news_list = News.objects.all()[start:limit]

    # json_list = []
    # json_dict = {}
    news_dict_list = []

    for news in news_list:
        news_dict = OrderedDict([
            ("title", news.title),
            ("thumb_url", news.thumb_url),
            ("url", news.pc_url),
        ])
        news_dict_list.append(news_dict)
        # json_dict.update({"title":news.title,"thumb_url":news.thumb_url})
        # json_list.append(json_dict)

    json_str = json.dumps(news_dict_list,ensure_ascii=False,indent=2)
    response = HttpResponse(json_str, content_type='application/json; charset=UTF-8',status=200)

    return response


