from flask import Flask, render_template
from app.my_list import list_bp
from app.my_list import list_index_bp
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(list_bp)  #注册蓝图
app.register_blueprint(list_index_bp)

db = SQLAlchemy(app, use_native_unicode='utf8')

@app.route("/")
def index():
    return render_template('首页.html')

if __name__ == "__main__":
    app.run(debug=True)