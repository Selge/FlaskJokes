from flask import Flask
from flask import render_template

from pyjoke import whysoserious, warumsoernst


app = Flask(__name__)


@app.route('/')
def index():
    Joker = whysoserious()
    Witzbold = warumsoernst()
    context = {Joker, Witzbold}
    return render_template("flaskjokes.html", context=context)


if __name__ == '__main__':
    app.run()
