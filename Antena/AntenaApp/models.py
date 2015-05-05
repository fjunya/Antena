# -*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin

"""
CATEGORY
1:エンタメ
2:スポーツ
3:アダルト
4:美女
5:お金・ギャンブル
"""

class News(models.Model):
    news_code = models.CharField("識別ID",max_length=200,blank=True,null=True)
    title = models.CharField("タイトル",max_length=200,blank=True,null=True)
    sub_title = models.CharField("サブタイトル",max_length=300,blank=True,null=True)
    content = models.TextField("記事全文",max_length=3000,blank=True,null=True)
    sub_content = models.TextField("記事の一部",max_length=1000,blank=True,null=True)
    thumb_url = models.CharField("サムネイル画像URL",max_length=200,blank=True,null=True)
    category = models.CharField("カテゴリ",max_length=50,blank=True,null=True)
    pub_date = models.DateTimeField("掲載日",blank=True,null=True)
    tag = models.CharField("タグ",max_length=100,blank=True,null=True)
    big_image_url = models.CharField("画像大URL",max_length=100,blank=True,null=True)
    pc_url = models.CharField("PC URL",max_length=200,blank=True,null=True)
    mobile = models.CharField("Mobile URL",max_length=200,blank=True,null=True)
    count = models.IntegerField("閲覧数",max_length=10,blank=True,null=True)
    day_count = models.IntegerField("1日の閲覧数",max_length=10,blank=True,null=True)
    site = models.CharField("雑誌名", max_length=100,blank=True,null=True)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('pk','news_code','title','site')

admin.site.register(News,NewsAdmin)