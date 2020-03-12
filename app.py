from flask import Flask, request
from flask import render_template

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    username = request.form.get('username') if request.method == "POST" else None
    return render_template('index.html', username=username)


if __name__ == '__main__':
    app.run()
