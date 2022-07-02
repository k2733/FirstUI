from flask import Flask, render_template
from app.my_list import list_bp

app = Flask(__name__)
app.register_blueprint(list_bp)


@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)