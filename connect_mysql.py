from flask import Flask, got_request_exception, render_template
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)

db = SQLAlchemy(app, use_native_unicode='utf8')
app.config.from_object(config)
# class Students(db.Model):
#     # 定义表名
#     __tablename__ = 'students'
#     # 定义字段
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(16))
#     stu_number = db.Column(db.String(32), unique=True)

#     def __repr__(self):
#         return '<User: %s %s %s %s>' % (self.name, self.id, self.stu_number)

# def create_table():
#         # 删除表
#         db.drop_all()
#         # 创建表
#         db.create_all()
        
#         stu1 = Students(name='小明', stu_number='1918101')
#         stu2 = Students(name='小红', stu_number='1918102')
#         stu3 = Students(name='小华', stu_number='1918103')
#         db.session.add_all([stu1,stu2,stu3])
#         db.session.commit()
#         return 

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

db.create_all()

@app.route('/')
def index():
    return 'Hello flask!'


if __name__ == '__main__':
    app.run(debug=True)
