# -*- coding: utf-8 -*-
#本地开发环境配置文件
from config.base_setting import *
#SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "mysql://root:wl45241397@127.0.0.1/manager_system"

SECRET_KEY = "imooc123456"


DOMAIN={
    "www":"http://127.0.0.1:5000"
}

RELEASE_PATH = "J:/flask\manager_sys/release_version"