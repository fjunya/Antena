# -*- coding: utf-8 -*-
__author__ = 'fjunya'
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from getSPAData import SPA
from getR25Data import R25
from models import News_Connection

def insertDb(news_list,session):
    for news in news_list:
        exist_count = session.query(News_Connection).filter(News_Connection.news_code == news['news_code']).count()
        if exist_count == 0:
            if news.has_key('title'):
                title = news['title']
            else:
                title = ''
            if news.has_key('sub_title'):
                sub_title = news['sub_title']
            else:
                sub_title = ''
            if news.has_key('content'):
                content = news['content']
            else:
                content = ''
            if news.has_key('sub_content'):
                sub_content = news['sub_content']
            else:
                sub_content = ''
            if news.has_key('thumb_url'):
                thumb_url = news['thumb_url']
            else:
                thumb_url = ''
            if news.has_key('category'):
                category = news['category']
            else:
                category = ''
            if news.has_key('pub_date'):
                pub_date = news['pub_date']
            else:
                pub_date = ''
            if news.has_key('tag'):
                tag = news['tag']
            else:
                tag = ''
            if news.has_key('big_image_url'):
                big_image_url = news['big_image_url']
            else:
                big_image_url = ''
            if news.has_key('pc_url'):
                pc_url = news['pc_url']
            else:
                pc_url = ''
            if news.has_key('mobile'):
                mobile = news['mobile']
            else:
                mobile = ''
            if news.has_key('site'):
                site = news['site']
            else:
                site = ''

            news_connection = News_Connection(
                news_code=news['news_code'],
                title=title,
                sub_title=sub_title,
                content=content,
                sub_content=sub_title,
                thumb_url=thumb_url,
                category=category,
                pub_date=pub_date,
                tag=tag,
                big_image_url=big_image_url,
                pc_url=pc_url,
                mobile=mobile,
                site=site,
            )

            session.add(news_connection)
            session.commit()


if __name__  == '__main__':
    #DBアクセス設定
    engine = create_engine('sqlite:///db.sqlite3')
    conn = engine.connect()
    session = sessionmaker(bind=engine)()

    #SPAからデータの取得
    spa = SPA()
    news_list = spa.getNews()
    insertDb(news_list,session)

    #R25からデータの取得
    r25 = R25()
    news_list = r25.getNews(category="06",count="100")
    insertDb(news_list,session)



