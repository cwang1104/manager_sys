from flask import Blueprint
from flask import request,jsonify
from application import app,db
import requests,json
from common.libs.DataHelper import getCurrentTime
from common.models.news import News

route_api = Blueprint("api_page",__name__)

@route_api.route("/all_news")

def all_news():
    resp = {'code':200,'msg':'操作成功！','data':{} }
    news_list = News.query.order_by(News.created_date.desc() ).all()
    swiper_list = News.query.limit(5).all()

    data_swiper=[]
    if swiper_list:
        for item in swiper_list:
            tmp_data={
                'id':item.id,
                # 'news_title':item.news_title,
                # 'news_src':item.news_src,
                'news_img':item.news_img,
                # 'news_desc':item.news_desc,
                'created_date':item.created_date.strftime("%Y-%m-%d")
            }
            data_swiper.append( tmp_data )

    resp['data']['swiper_list']=data_swiper

    data_news = []
    if news_list:
        for item in news_list:
            tmp_data={
                'id':item.id,
                'news_title':item.news_title,
                'news_src':item.news_src,
                'news_img':item.news_img,
                'news_desc':item.news_desc,
                'created_date':item.created_date.strftime("%Y-%m-%d")
            }
            data_news.append( tmp_data )

    resp['data']['news_list']=data_news

    return jsonify(resp)

@route_api.route("/id_news",methods=["GET",'POST'])

def id_news():
    req = request.values
    news_id = int(req['id']) if 'id' in req else 0
    resp = {'code':200,'msg':'操作成功！','data':{} }
    news = News.query.filter_by(id=news_id).first()
    resp['data']={
        'id':news.id,
        'news_title':news.news_title,
        'news_src':news.news_src,
        'news_img':news.news_img,
        'news_desc':news.news_desc,
        'created_date':news.created_date.strftime("%Y-%m-%d")
    }
    return jsonify(resp)