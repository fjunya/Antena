__author__ = 'fukagawa'

import requests

class R25:

    def __init__(self):
        self.auth_key = "a0fcb9bda5e5f19a"
        self.url = "http://webservice.recruit.co.jp/r25/"

    def getNews(self,category=None,tag=None,search_word=None,start="1"):
        request_url = self.url + "article/v1?type=full"
        if category:
            request_url += "&category=" + category
        if tag:
            request_url += "&tag=" + tag
        if search_word:
            request_url += "&keyword=" + search_word
        request_url += "&start=" + start + "&key=" + self.auth_key

        print(request_url)

        response = requests.get(request_url)

        return response

if __name__  == '__main__':
    r25 = R25()
    res = r25.getNews(category="01")
    print(res.text)







