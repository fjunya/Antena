from django.shortcuts import render

from form import NewsForm
from django.http import JsonResponse
from models import News

def top(request):
    form = NewsForm()
    return JsonResponse({'result': 'ok'})

def putNews(request,start=1,limit=30,search=None):
    if search:
        news = News.objects.filter(title=search).filter(
                                        content=search)[start:start+limit]
    else:
        news = News.objects.all()[start:start+limit]

    for i in news:
