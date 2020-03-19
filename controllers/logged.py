from flask import Blueprint,render_template,request
from common.libs.Helper import ops_render,ops_renderJSON,iPagenation
from common.models.user import User
from common.models.news import News
from common.models.cars_info import CarsInfo
from common.libs.DataHelper import getCurrentTime
from application import db,app
import math
logged_page = Blueprint("logged_page",__name__)

@logged_page.route("/main")
def logged_main_page():
    query_news = News.query
    query_cars = CarsInfo.query

    news_num = query_news.count()
    cars_num = query_cars.count()

    numbers={
        "news_num":news_num,
        "cars_num":cars_num
    }
    return ops_render("func/main.html",{"numbers":numbers})

@logged_page.route("/goods")
def goods_page():
    req = request.values
    order_by_g = str(req['order']) if ("order" in req and req['order']) else 'lastest'

    page = 1
    if 'p' in req and req['p']:
        page = int(req['p'])
    query = CarsInfo.query
    page_params = {
        'total_count': query.count(),
        'page_size': 12,
        'page': page,
        'url': "/logged/goods?"
    }
    pages = iPagenation(page_params)

    offset = (page - 1) * page_params['page_size']
    limit = page * page_params['page_size']
    if order_by_g =="hot":
        query = query.order_by(CarsInfo.id.desc())
    else:
        query = query.order_by(-CarsInfo.id.desc())
    list_goods = query[offset:limit]

    return ops_render("func/goods.html", {"data": list_goods, "pages": pages})

@logged_page.route("/goods_info",methods=["GET","POST"])
def goods_info_page():
    # req = request.values    #1
    # id = int(req['id']) if ('id' in req and req['id']) else 0
    # info = CarsInfo.query.filter_by(id=id).first()
    # return ops_render("func/goods_info.html", {"info":info})

    # req = request.values  # 1
    # id = int(req['id']) if ('id' in req and req['id']) else 0  # 2
    # news_id = req['news_id'] if "news_id" in req else ""
    # if request.method == "GET":
    #     info = News.query.filter_by(id=id).first()  # 3
    #     return ops_render("func/news_info.html", {"info": info})
    # if request.method == "POST":
    #     news = News.query.get(news_id)
    #     db.session.delete(news)
    #     db.session.commit()
    #     return ops_renderJSON(msg="删除成功")

    req = request.values    #1
    id = int(req['id']) if ('id' in req and req['id']) else 0 #2
    goods_id = req['goods_id'] if "goods_id" in req else ""
    if request.method =="GET":
        info = CarsInfo.query.filter_by(id=id).first() #3
        return ops_render("func/goods_info.html", {"info": info})
    if request.method =="POST":
        cars = CarsInfo.query.get(goods_id)
        db.session.delete(cars)
        db.session.commit()
        return ops_renderJSON(msg="删除成功")

@logged_page.route("/goods_add",methods=["GET","POST"])
def goods_add_page():
    if request.method == "GET":
        return ops_render("func/goods_add.html")
    req = request.values  # 如果值在里面则取，不在则取空
    title = req['title'] if "title" in req else ""
    brand = req['brand'] if "brand" in req else ""
    arctic = req['arctic'] if "arctic" in req else ""
    regist_date = req['regist_date'] if "regist_date" in req else ""
    mileage = req['mileage'] if "mileage" in req else ""
    emissions = req['emissions'] if "emissions" in req else ""
    gear = req['gear'] if "gear" in req else ""
    price = req['price'] if "price" in req else ""
    cars_local = req['cars_local'] if "cars_local" in req else ""
    describe = req['describe'] if "describe" in req else ""
    img_desc = req['img_desc'] if "img_desc" in req else ""
    picture2 = req['picture2'] if "picture2" in req else ""
    picture3 = req['picture3'] if "picture3" in req else ""
    picture4 = req['picture4'] if "picture4" in req else ""
    picture5 = req['picture5'] if "picture5" in req else ""
    picture6 = req['picture6'] if "picture6" in req else ""
    picture1 = req['picture1'] if "picture1" in req else ""

    model_cars_info = CarsInfo()  # model实例化
    model_cars_info.title = title
    model_cars_info.describe = describe
    model_cars_info.picture3 = picture3
    model_cars_info.picture1 = picture1
    model_cars_info.img_desc = img_desc
    model_cars_info.picture6 = picture6
    model_cars_info.picture5 = picture5
    model_cars_info.cars_local = cars_local
    model_cars_info.picture4 = picture4
    model_cars_info.picture2 = picture2
    model_cars_info.price = price
    model_cars_info.mileage = mileage
    model_cars_info.gear = gear
    model_cars_info.emissions = emissions
    model_cars_info.brand = brand
    model_cars_info.arctic = arctic
    model_cars_info.regist_date = regist_date

    model_cars_info.created_date = getCurrentTime()
    db.session.add(model_cars_info)
    db.session.commit()

    return ops_renderJSON(msg="提交成功！")

    name = "imooc"
    context = {"name": name}

    return ops_render("func/goods_add.html", context)

@logged_page.route("/goods_del")
def goods_del_page():
    name = "imooc"
    context = {"name": name}
    result = User.query.all()
    context['result'] = result
    return ops_render("func/goods_del.html", context)

@logged_page.route("/goods_mod")
def goods_mod_page():
    name = "imooc"
    context = {"name": name}
    result = User.query.all()
    context['result'] = result
    return ops_render("func/goods_mod.html", context)

@logged_page.route("/news")
def news_page():

    req=request.values
    order_by_f = str(req['order']) if ("order" in req and req['order']) else 'lastest'
    page=1
    if 'p' in req and req['p']:
        page=int(req['p'])
    query = News.query
    page_params={
        'total_count':query.count(),
        'page_size':12,
        'page':page,
        'url':"/logged/news?"
    }
    pages=iPagenation(page_params)

    offset = (page-1) * page_params['page_size']
    limit = page * page_params['page_size']

    if order_by_f =="hot":
        query = query.order_by(News.id.desc())
    else:
        query = query.order_by(-News.id.desc())
    list_news =query[offset:limit]

    return ops_render("func/news.html",{"data":list_news,"pages":pages})




@logged_page.route("/news_info",methods=["GET","POST"])
def news_info_page():
    req = request.values    #1
    id = int(req['id']) if ('id' in req and req['id']) else 0 #2
    news_id = req['news_id'] if "news_id" in req else ""
    if request.method =="GET":
        info = News.query.filter_by(id=id).first() #3
        return ops_render("func/news_info.html", {"info": info})
    if request.method =="POST":
        news = News.query.get(news_id)
        db.session.delete(news)
        db.session.commit()
        return ops_renderJSON(msg="删除成功")





@logged_page.route("/news_add",methods=["GET","POST"])
def news_add_page():

    if request.method =="GET":
        return ops_render("func/news_add.html")
    req = request.values  # 如果值在里面则取，不在则取空
    news_title = req['news_title'] if "news_title" in req else ""
    news_img = req['news_img'] if "news_img" in req else ""
    news_src = req['news_src'] if "news_src" in req else ""
    news_desc = req['news_desc'] if "news_desc" in req else ""

    model_news = News()   #model实例化
    model_news.news_title= news_title
    model_news.news_img= news_img
    model_news.news_src= news_src
    model_news.news_desc= news_desc
    model_news.created_date=getCurrentTime()
    db.session.add(model_news)
    db.session.commit()

    return ops_renderJSON(msg="提交成功！")


@logged_page.route("/news_del")
def news_del_page():
    name = "imooc"
    context = {"name": name}
    result = User.query.all()
    context['result'] = result
    return ops_render("func/news_del.html", context)

@logged_page.route("/news_mod")
def news_mod_page():
    name = "imooc"
    context = {"name": name}
    result = User.query.all()
    context['result'] = result
    return ops_render("func/news_mod.html", context)