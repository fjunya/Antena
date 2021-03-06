# -*- coding: utf-8 -*-
__author__ = 'fukagawa'

"""
Category
01:ライフ・マネー
02:ビジネス・経済
03:政治・社会
04:IT・サイエンス
05:トリビア
06:カルチャー・エンタメ
07:スポーツ・レジャー
"""

import requests
from xml.etree import ElementTree
from datetime import datetime

class R25:

    def __init__(self):
        self.auth_key = "a0fcb9bda5e5f19a"
        self.url = "http://webservice.recruit.co.jp/r25/"

    def getNews(self,category=None,tag=None,search_word=None,count="100",start="1"):
        """
        ニュースデータをlist型で返す。リストの中は辞書型となる。
        :param category: String
        :param tag: String
        :param search_word: String
        :param count: String
        :param start: String
        :return:[]
        """
        request_url = self.url + "article/v1?type=full"
        return_list = []
        if category:
            request_url += "&category=" + category
        if tag:
            request_url += "&tag=" + tag
        if search_word:
            request_url += "&keyword=" + search_word
        request_url += "&start=" + start + "&key=" + self.auth_key + "&count=" + count
        try:
            response = requests.get(request_url).text.encode('utf-8')
        except:
            return return_list

        xml_root = ElementTree.fromstring(response)

        tag_list = [['news_code','code'],['title','headline'],['sub_title','sub_headline'],
            ['sub_content','snippet'],['thumb_url','thumb'],['pub_date','pub_date'],
            ['tag','tag']]
        for xml_child1 in xml_root:
            dict = {}
            for tag in tag_list:
                dict.update({tag[0]:""})
            if len(xml_child1.getchildren()) != 0:
                for xml_child2 in xml_child1:
                    for tag in tag_list:
                        if xml_child2.tag.find(tag[1]) != -1:
                            dict.update({tag[0] : xml_child2.text})
                            if tag[0] == "thumb_url":
                                dict.update({"content":""})
                                dict.update({"big_image_url":""})
                                #雑誌名の追加
                                dict.update({'site':u'R25'})
                                return_list.append(dict)
                                break
                            elif tag[0] == 'pub_date':
                                pub_date = datetime.strptime(xml_child2.text, '%Y%m%d')
                                dict.update({tag[0] : pub_date})
                            elif tag[0] == 'tag':
                                if xml_child2.text in [u'今日の彼女',u'美女']:
                                    dict.update({'tag' : u'美女'})
                                else:
                                    dict.update({'tag' : u'エンタメ'})


                    if xml_child2.tag.find("urls") != -1:
                        for xml_child3 in xml_child2.getchildren():
                            if xml_child3.tag.find("pc") != -1:
                                dict.update({"pc_url" : xml_child3.text})
                                dict.update({"mobile" : xml_child3.text})
                    # elif xml_child2.tag.find("category") != -1:
                    #     for xml_child4 in xml_child2.getchildren():
                    #         if xml_child4.tag.find("name"):
                    #             dict.update({"category" : xml_child4.text})
        return return_list

    def getCategory(self):
        """
        カテゴリー一覧を取得
        :return:
        """
        request_url = self.url + "category/v1?key=" + self.auth_key
        return requests.get(request_url)







