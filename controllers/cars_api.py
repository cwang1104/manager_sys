from flask import Blueprint, jsonify, request
from common.models.cars_info import CarsInfo

cars_api = Blueprint("cars_api", __name__)


@cars_api.route("/all_cars")
def all_cars():
    resp = {'code': 200, 'msg': '操作成功！', 'data': {}}
    cars_list = CarsInfo.query.order_by(CarsInfo.created_date.desc()).all()
    cars_list_price = CarsInfo.query.order_by(CarsInfo.price).all()
    cars_list_mile = CarsInfo.query.order_by(CarsInfo.mileage.desc()).all()

    # 里程数最少
    data_cars_mile = []
    if cars_list_mile:
        for item in cars_list_mile:
            tmp_data = {
                'id': item.id,
                'title': item.title,
                'brand': item.brand,
                'cars_local': item.cars_local,
                'arctic': item.arctic,
                'regist_date': item.regist_date,
                'mileage': int(item.mileage),
                'gear': item.gear,
                'emissions': item.emissions,
                'price': item.price,
                'img_desc': item.img_desc,
                'describe': item.describe,
                'picture1': item.picture1,
                'picture2': item.picture2,
                'picture3': item.picture3,
                'picture4': item.picture4,
                'picture5': item.picture5,
                'picture6': item.picture6,

                'created_date': item.created_date.strftime("%Y-%m-%d")
            }
            data_cars_mile.append(tmp_data)

    resp['data']['cars_list_mile'] = data_cars_mile

    # 价格排序
    data_cars_price = []
    if cars_list_price:
        for item in cars_list_price:
            tmp_data = {
                'id': item.id,
                'title': item.title,
                'brand': item.brand,
                'cars_local': item.cars_local,
                'arctic': item.arctic,
                'regist_date': item.regist_date,
                'mileage': item.mileage,
                'gear': item.gear,
                'emissions': item.emissions,
                'price': item.price,
                'img_desc': item.img_desc,
                'describe': item.describe,
                'picture1': item.picture1,
                'picture2': item.picture2,
                'picture3': item.picture3,
                'picture4': item.picture4,
                'picture5': item.picture5,
                'picture6': item.picture6,

                'created_date': item.created_date.strftime("%Y-%m-%d")
            }
            data_cars_price.append(tmp_data)

    resp['data']['cars_list_price'] = data_cars_price

    # 上架时间排序
    data_cars = []
    if cars_list:
        for item in cars_list:
            tmp_data = {
                'id': item.id,
                'title': item.title,
                'brand': item.brand,
                'cars_local': item.cars_local,
                'arctic': item.arctic,
                'regist_date': item.regist_date,
                'mileage': item.mileage,
                'gear': item.gear,
                'emissions': item.emissions,
                'price': item.price,
                'img_desc': item.img_desc,
                'describe': item.describe,
                'picture1': item.picture1,
                'picture2': item.picture2,
                'picture3': item.picture3,
                'picture4': item.picture4,
                'picture5': item.picture5,
                'picture6': item.picture6,

                'created_date': item.created_date.strftime("%Y-%m-%d")
            }
            data_cars.append(tmp_data)

    resp['data']['cars_list'] = data_cars

    return jsonify(resp)


@cars_api.route("/id_cars", methods=["POST", 'GET'])
def id_cars():
    req = request.values
    cars_id = int(req['id']) if 'id' in req else 0
    resp = {'code': 200, 'msg': '操作成功！', 'data': {}}
    cars = CarsInfo.query.filter_by(id=cars_id).first()
    resp['data'] = {
        'id': cars.id,
        'title': cars.title,
        'brand': cars.brand,
        'cars_local': cars.cars_local,
        'arctic': cars.arctic,
        'regist_date': cars.regist_date,
        'mileage': cars.mileage,
        'gear': cars.gear,
        'emissions': cars.emissions,
        'price': cars.price,
        'img_desc': cars.img_desc,
        'describe': cars.describe,
        'picture1': cars.picture1,
        'picture2': cars.picture2,
        'picture3': cars.picture3,
        'picture4': cars.picture4,
        'picture5': cars.picture5,
        'picture6': cars.picture6,
        'created_date': cars.created_date.strftime("%Y-%m-%d")
    }
    return jsonify(resp)