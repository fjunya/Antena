# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('news_code', models.CharField(max_length=200, blank=True, verbose_name='識別ID')),
                ('title', models.CharField(max_length=200, blank=True, verbose_name='タイトル')),
                ('sub_title', models.CharField(max_length=300, blank=True, verbose_name='サブタイトル')),
                ('content', models.TextField(max_length=3000, blank=True, verbose_name='記事全文')),
                ('sub_content', models.TextField(max_length=1000, blank=True, verbose_name='記事の一部')),
                ('thumb_url', models.CharField(max_length=200, blank=True, verbose_name='サムネイル画像URL')),
                ('category', models.CharField(max_length=50, blank=True, verbose_name='カテゴリ')),
                ('pub_date', models.DateTimeField(blank=True, verbose_name='掲載日')),
                ('tag', models.CharField(max_length=100, blank=True, verbose_name='タグ')),
                ('big_image_url', models.CharField(max_length=100, blank=True, verbose_name='画像大URL')),
                ('pc_url', models.CharField(max_length=200, blank=True, verbose_name='PC URL')),
                ('mobile', models.CharField(max_length=200, blank=True, verbose_name='Mobile URL')),
                ('count', models.IntegerField(max_length=10, blank=True, verbose_name='閲覧数')),
                ('day_count', models.IntegerField(max_length=10, blank=True, verbose_name='1日の閲覧数')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
