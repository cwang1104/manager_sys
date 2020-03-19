from application import app,db
from flask import Blueprint,render_template,request,make_response,redirect
from common.libs.Helper import ops_renderJSON,ops_renderErrorJSON,ops_render
from common.libs.DataHelper import getCurrentTime
from common.libs.UrlManager import UrlManger
from common.models.user import User
from common.libs.UserService import UserService


member_page= Blueprint("member_page",__name__)

@member_page.route("/reg",methods=["GET","POST"])
def reg():
    if request.method =="GET":
        return ops_render("member/reg.html")
    req = request.values  # 如果值在里面则取，不在则取空
    login_name = req['login_name'] if "login_name" in req else ""
    login_pwd = req['login_pwd'] if "login_pwd" in req else ""
    login_pwd2 = req['login_pwd2'] if "login_pwd2" in req else ""

    #后端输入验证
    if login_name is None or len(login_name) <1:
        return ops_renderErrorJSON(msg="请输入正确的管理员账户名")
    if login_pwd is None or len(login_pwd)<6:
        return ops_renderErrorJSON(msg="请正确输入管理员账户密码，并且不能小于6个字符！")
    if login_pwd != login_pwd2:
        return ops_renderErrorJSON(msg="请确认管理员账户密码！")
    #后端数据库信息验证

    user_info = User.query.filter_by(login_name = login_name).first()
    if user_info:
        return ops_renderErrorJSON(msg="此管理员账户名已存在，请重新输入！")

    model_user = User()   #model实例化
    model_user.login_name= login_name
    model_user.login_salt=UserService.geneSalt(8)
    model_user.login_pwd=UserService.genePwd(login_pwd,model_user.login_salt)
    model_user.created_time=model_user.updated_time=getCurrentTime()
    db.session.add(model_user)
    db.session.commit()

    return ops_renderJSON(msg="注册提交成功，等待审核！")




@member_page.route("/login",methods=["GET","POST"])
def login():
    if request.method =="GET":
        return ops_render("member/login.html")
    req = request.values
    login_name = req['login_name'] if 'login_name' in req else ""
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ""

    if login_name is None or len(login_name)<1:
        return ops_renderErrorJSON("请输入正确的管理员账户名！")

    if login_pwd is None or len(login_pwd)<6:
        return ops_renderErrorJSON("请输入正确的密码！")

    user_info = User.query.filter_by(login_name=login_name).first()
    if not user_info:
        return ops_renderErrorJSON("请输入正确的管理员账户名和密码！")

    if user_info.login_pwd != UserService.genePwd(login_pwd,user_info.login_salt):
        return ops_renderErrorJSON("请输入正确的管理员账户名或密码！")
    if user_info.status !=1:
        return ops_renderErrorJSON("账户被禁用，请联系技术管理员解决！")

    response = make_response(ops_renderJSON(msg="登录成功！"))
    response.set_cookie(app.config['AUTH_COOKIE_NAME'],"%s#%s"%(UserService.geneAuthCode( user_info ),user_info.id),60*60*24*120)
    return response


@member_page.route("/logout")
def logout():

    response= make_response(redirect(UrlManger.buildUrl("/member/login")))
    response.delete_cookie(app.config['AUTH_COOKIE_NAME'])
    return response

@member_page.route("/reg1")
def reg1():
    return render_template("system/reg1.html")