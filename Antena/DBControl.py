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
        pass

    def insert(self,dict):

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
