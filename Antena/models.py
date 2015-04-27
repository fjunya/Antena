# -*- coding: utf-8 -*-

__author__ = 'fukagawa'

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.dialects.sqlite import DATETIME,VARCHAR,INTEGER,TEXT
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker

Base = declarative_base()

class News_Connection(Base):
    __tablename__ = 'AntenaApp_news'

    id = Column('id', INTEGER, primary_key=True)
    news_code = Column('news_code',VARCHAR)
    title = Column('title',VARCHAR)
    sub_title = Column('sub_title', VARCHAR)
    content = Column('content',TEXT)
    sub_content = Column('sub_content',TEXT)
    thumb_url = Column('thumb_url',VARCHAR)
    category = Column('category',VARCHAR)
    pub_date = Column('pub_date', DATETIME)
    tag = Column('tag',VARCHAR)
    big_image_url = Column('big_image_url',VARCHAR)
    pc_url = Column('pc_url',VARCHAR)
    mobile = Column('mobile',VARCHAR)
    count = Column('count',INTEGER)
    day_count = Column('day_count',INTEGER)


if __name__  == '__main__':
    engine = create_engine('sqlite:///db.sqlite3')
    conn = engine.connect()
    session = sessionmaker(bind=engine)()

    resultData = session.query(News_Connection).filter(News_Connection.id == 1)
    for row in resultData:
        print row.title

    news_connection = News_Connection(
        title='test'
    )

    session.add(news_connection)
    session.commit()

