from django.db import models

class News(models.Model):
    news_code = models.CharField("識別ID",max_length=200,blank=True)
    title = models.CharField("タイトル",max_length=200,blank=True)
    sub_title = models.CharField("サブタイトル",max_length=300,blank=True)
    content = models.TextField("記事全文",max_length=3000,blank=True)
    sub_content = models.TextField("記事の一部",max_length=1000,blank=True)
    thumb_url = models.CharField("サムネイル画像URL",max_length=200,blank=True)
    category = models.CharField("カテゴリ",max_length=50,blank=True)
    pub_date = models.DateTimeField("掲載日",blank=True)
    tag = models.CharField("タグ",max_length=100,blank=True)
    big_image_url = models.CharField("画像大URL",max_length=100,blank=True)
    pc_url = models.CharField("PC URL",max_length=200,blank=True)
    mobile = models.CharField("Mobile URL",max_length=200,blank=True)
    count = models.IntegerField("閲覧数",max_length=10,blank=True)
    day_count = models.IntegerField("1日の閲覧数",max_length=10,blank=True)