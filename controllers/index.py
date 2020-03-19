# -*- coding: utf-8 -*-
from flask import Blueprint,render_template
from common.models.user import User
from common.libs.Helper import ops_render
index_page = Blueprint( "index_page",__name__ )

@index_page.route("/")
def index():
    ##传值
    name = "imooc"
    ##
    context = { "name" : name }


    return ops_render( "index.html",context )

