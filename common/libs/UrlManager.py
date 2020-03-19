from application import app
from common.libs.DataHelper import getCurrentTime
import os

class UrlManger(object):  # 都生成绝对路径
    @staticmethod
    def buildUrl(path):  # 生成网页跳转地址
        config_domain = app.config['DOMAIN']
        return "%s%s" % (config_domain['www'], path)

    @staticmethod  # 生成静态文件加载地址
    def buildStaticUrl(path):
        path = "/static" + path +'?ver=' +UrlManger.getReleaseVersion()
        return UrlManger.buildUrl(path)

    @staticmethod
    def getReleaseVersion():
        ver = "%s"%( getCurrentTime("%Y%m%d%H%M%S%f") )
        release_path = app.config.get('RELEASE_PATH')
        if release_path and os.path.exists( release_path ):
            with open(release_path,'r') as f:
                ver=f.readline()
        return ver