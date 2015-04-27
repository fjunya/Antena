# -*- coding: utf-8 -*-
__author__ = 'fjunya'

import sqlite3
import datetime



# from sqlalchemy import create_engine,Column,String,Integer,VARCHAR,Text,DateTime
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
# Base = declarative_base()
#
# class AntenaApp_news(Base):
#
#     __tablename__ = 'AntenaApp_news'
#
#     id = Column(Integer, primary_key=True)
#     news_code = Column(VARCHAR)
#     title = Column(VARCHAR)
#     sub_title = Column(VARCHAR)
#     content = Column(Text)
#     sub_content = Column(Text)
#     thumb_url = Column(VARCHAR)
#     category = Column(VARCHAR)
#     pub_date = Column(DateTime)
#     tag = Column(VARCHAR)
#     big_image_url = Column(VARCHAR)
#     pc_url = Column(VARCHAR)
#     mobile = Column(VARCHAR)
#     count = Column(Integer)
#     day_count = Column(Integer)



class SqliteControl:

    def __init__(self):
        # Session = sessionmaker()
        # engine = create_engine('sqlite:///db.sqlite3')
        # Session.configure(bind=engine)
        # self.session = Session()
        # self.News = AntenaApp_news()

        pass

    def insert(self,dict):

        # print dict

        # data = self.session.query(self.News).filter(id=1)


        # query = 'INSERT INTO AntenaApp_news VALUES(%(news_code)s,%(title)s,' \
        #         '%(sub_title)s,%(content)s,%(sub_content)s,%(thumb_url)s,' \
        #         '%(category)s,%(pub_date)s,%(tag)s,%(big_image_url)s,' \
        #         '%(pc_url)s,%(mobile)s,%(count)s,%(day_count)s)' % \
        #         {"news_code":dict['news_code'],"title":dict['title'],
        #         "sub_title":dict['sub_title'],"content":dict['content'],
        #         "sub_content":dict['sub_content'],"thumb_url":dict['thumb_url'],
        #         "category":dict['category'],"pub_date":dict['pub_date'],
        #         "tag":dict['tag'],"big_image_url":dict['big_image_url'],
        #         "pc_url":dict['pc_url'],"mobile":dict['mobile'],
        #         "count":0,"day_count":0
        #         }

        # query = 'INSERT INTO AntenaApp_news VALUES(%(news_code)s,"%(title)s",' \
        #         '"%(sub_title)s","%(content)s","%(sub_content)s","%(thumb_url)s",' \
        #         '"%(category)s","%(pub_date)s","%(tag)s,%(big_image_url)s",' \
        #         '"%(pc_url)s",%(mobile)s,%(count)s,%(day_count)s)' % \
        #         {"news_code":dict['news_code'],"title":dict['title'],
        #         "sub_title":dict['sub_title'],"content":" ",
        #         "sub_content":" ","thumb_url":dict['thumb_url'],
        #         "category":dict['category'],"pub_date":dict['pub_date'],
        #         "tag":dict['tag'],"big_image_url":dict['big_image_url'],
        #         "pc_url":dict['pc_url'],"mobile":dict['mobile'],
        #         "count":0,"day_count":0
        #         }

        query = 'INSERT INTO AntenaApp_news(news_code,' \
                                            'title,' \
                                            'sub_title,' \
                                            'content,' \
                                            'sub_content,' \
                                            'thumb_url,' \
                                            'category,' \
                                            'tag,' \
                                            'big_image_url,' \
                                            'pc_url,' \
                                            'mobile,' \
                                            'count,' \
                                            'day_count) VALUES (%s,"%s","%s","%s","%s","%s","%s","%s","%s","%s","%s",%d,%d)' % \
                                            (dict['news_code'],
                                             dict['title'],
                                             dict['sub_title'],
                                             dict['content'],
                                             dict['sub_content'],
                                             dict['thumb_url'],
                                             dict['category'],
                                             dict['tag'],
                                             dict['big_image_url'],
                                             dict['pc_url'],
                                             dict['mobile'],
                                             0,
                                             0)


        print(query)
        #
        con = sqlite3.connect("db.sqlite3")
        con.execute(query)
        con.commit()
        con.close()
