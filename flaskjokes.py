from flask import Flask
from flask import render_template

from pyjoke import whysoserious


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("flaskjokes.html")


if __name__ == '__main__':
    app.run()
