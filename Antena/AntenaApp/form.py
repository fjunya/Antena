# -*- coding: utf-8 -*-
__author__ = 'fjunya'

from django.forms import ModelForm
from models import News

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['news_code','title','sub_title',
                  'content','sub_content','thumb_url',
                  'category','pub_date','tag',
                  'big_image_url','pc_url','mobile',
                  'count','day_count']
