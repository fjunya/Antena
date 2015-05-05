# -*- coding: utf-8 -*-

__author__ = 'fjunya'

import feedparser
import re
from datetime import datetime

class Bunsyun:

    def __init__(self):
        RSS_URL = "http://shukan.bunshun.jp/list/feed/rss"
        self.feed = feedparser.parse(RSS_URL)

    def getNews(self):
        """
        :return:[]
        """
        return_list = []
        for entry in self.feed["entries"]:
            dict = {}
            news_code = entry.id
            dict.update({'news_code':news_code})
            title = entry.title
            dict.update({'title':title})
            # thumb_url = re.findall(r'img src="(.+?)"', entry.content[0].value)[0]
            # dict.update({'thumb_url':thumb_url})

            #catetoryの取得
            category = u'エンタメ'
            dict.update({'category':category})

            #更新日の取得
            tmp = entry.published_parsed
            pub_date = datetime.strptime(str(tmp.tm_year) + '-' + str(tmp.tm_mon) +  '-' +
                                         str(tmp.tm_mday) + ' ' + str(tmp.tm_hour) + ':' +
                                         str(tmp.tm_min) + ':00', '%Y-%m-%d %H:%M:%S')
            dict.update({'pub_date':pub_date})

            #URLの取得
            pc_url = entry.link
            dict.update({'pc_url':pc_url})
            mobile = entry.link
            dict.update({'mobile':mobile})

            #雑誌名の追加
            dict.update({'site' : u"文春"})

            return_list.append(dict)

        return return_list


if __name__  == '__main__':
    bunsyun = Bunsyun()
    news_list = bunsyun.getNews()
    print(news_list)


