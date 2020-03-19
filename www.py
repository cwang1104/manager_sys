# -*- coding: utf-8 -*-
from application import app


from flask_debugtoolbar import DebugToolbarExtension
toolbar = DebugToolbarExtension( app )

'''
拦截器处理 和 错误处理器
'''
from interceptors.Auth import *
from interceptors.errorHandler import *

'''
蓝图引入
'''

from controllers.index import index_page
from controllers.member import member_page
from controllers.logged import logged_page
from controllers.news_api import route_api
from controllers.cars_api import cars_api
app.register_blueprint( index_page,url_prefix = "/" )
app.register_blueprint( member_page,url_prefix="/member")
app.register_blueprint( logged_page,url_prefix="/logged")
app.register_blueprint( route_api,url_prefix="/api")
app.register_blueprint( cars_api,url_prefix="/cars_api")

'''
模板函数，全局注入
'''
from common.libs.UrlManager import UrlManger
app.add_template_global(UrlManger.buildUrl,"buildUrl")
app.add_template_global(UrlManger.buildStaticUrl,"buildStaticUrl")