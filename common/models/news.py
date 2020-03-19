# coding: utf-8
from application import db

class News(db.Model):
    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    news_title = db.Column(db.String(collation='utf8mb4_bin'), info='??')
    news_src = db.Column(db.String(200, 'utf8mb4_bin'), info='????')
    news_img = db.Column(db.String(200, 'utf8mb4_bin'), info='?????')
    news_desc = db.Column(db.String(200, 'utf8mb4_bin'), info='??')
    created_date = db.Column(db.DateTime, info='????')

    def __init__(self, **items):
        for key in items:
            if hasattr(self, key):
                setattr(self, key, items[key])