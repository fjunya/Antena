# -*- coding: utf-8 -*-
__author__ = 'fjunya'

import feedparser
import re
from datetime import datetime



class SPA:

    def __init__(self):
        RSS_URL = "http://nikkan-spa.jp/feed"
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
            thumb_url = re.findall(r'img src="(.+?)"', entry.content[0].value)[0]
            dict.update({'thumb_url':thumb_url})

            #catetoryの取得
            category = None
            for tag in entry.tags:
                if tag.term in [u'エンタメ',]:
                    category = u'エンタメ'
                    break
                elif tag.term in [u'野球',u'サッカー',u'アスリート',u'スポーツ']:
                    category = u'スポーツ'
                    break
                elif tag.term in [u'AV女優',u'セクシー',u'性生活',u'性風俗',u'デリヘル嬢']:
                    category = u'アダルト'
                    break
                elif tag.term in [u'競艇',u'公営ギャンブル',u'ボートレース',u'競馬',u'競輪',u'マネー']:
                    category = u'ギャンブル'
                    break
            if not category:
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
            dict.update({'site' : u"SPA"})

            return_list.append(dict)

        return return_list




