from flask import Blueprint,render_template

list_bp = Blueprint("list",__name__,url_prefix="/list")  #前缀后的路由

@list_bp.route("/")  #前缀
def my_list():
    return render_template("list.html")