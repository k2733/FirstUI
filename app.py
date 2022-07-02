from flask import Flask, render_template
from app.my_list import list_bp
from app.my_list import list_index_bp

app = Flask(__name__)
app.register_blueprint(list_bp)  #注册蓝图
app.register_blueprint(list_index_bp)


@app.route("/")
def index():
    return render_template('首页.html')

if __name__ == "__main__":
    app.run(debug=True)