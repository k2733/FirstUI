from flask import Blueprint,render_template

list_bp = Blueprint("list",__name__,url_prefix="/list")  #url_predix指定蓝图路由前缀
list_index_bp = Blueprint("index",__name__,url_prefix="/index")  

@list_bp.route("/")
def list():
    return render_template("list.html")

@list_bp.route("/one")  #指定蓝图路由前缀后的路由
def my_list():
    return render_template("list_one.html")

@list_index_bp.route("/")
def list_index():
    return render_template("index.html")

@list_index_bp.route("/one")
def my_list_index():
    return render_template("index_one.html")