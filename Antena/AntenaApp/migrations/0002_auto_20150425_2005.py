# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AntenaApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='big_image_url',
            field=models.CharField(max_length=100, null=True, verbose_name=b'\xe7\x94\xbb\xe5\x83\x8f\xe5\xa4\xa7URL', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe3\x82\xab\xe3\x83\x86\xe3\x82\xb4\xe3\x83\xaa', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(max_length=3000, null=True, verbose_name=b'\xe8\xa8\x98\xe4\xba\x8b\xe5\x85\xa8\xe6\x96\x87', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='count',
            field=models.IntegerField(max_length=10, null=True, verbose_name=b'\xe9\x96\xb2\xe8\xa6\xa7\xe6\x95\xb0', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='day_count',
            field=models.IntegerField(max_length=10, null=True, verbose_name=b'1\xe6\x97\xa5\xe3\x81\xae\xe9\x96\xb2\xe8\xa6\xa7\xe6\x95\xb0', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='mobile',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Mobile URL', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='news_code',
            field=models.CharField(max_length=200, null=True, verbose_name=b'\xe8\xad\x98\xe5\x88\xa5ID', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='pc_url',
            field=models.CharField(max_length=200, null=True, verbose_name=b'PC URL', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name=b'\xe6\x8e\xb2\xe8\xbc\x89\xe6\x97\xa5', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='sub_content',
            field=models.TextField(max_length=1000, null=True, verbose_name=b'\xe8\xa8\x98\xe4\xba\x8b\xe3\x81\xae\xe4\xb8\x80\xe9\x83\xa8', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='sub_title',
            field=models.CharField(max_length=300, null=True, verbose_name=b'\xe3\x82\xb5\xe3\x83\x96\xe3\x82\xbf\xe3\x82\xa4\xe3\x83\x88\xe3\x83\xab', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='tag',
            field=models.CharField(max_length=100, null=True, verbose_name=b'\xe3\x82\xbf\xe3\x82\xb0', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='thumb_url',
            field=models.CharField(max_length=200, null=True, verbose_name=b'\xe3\x82\xb5\xe3\x83\xa0\xe3\x83\x8d\xe3\x82\xa4\xe3\x83\xab\xe7\x94\xbb\xe5\x83\x8fURL', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=200, null=True, verbose_name=b'\xe3\x82\xbf\xe3\x82\xa4\xe3\x83\x88\xe3\x83\xab', blank=True),
            preserve_default=True,
        ),
    ]
