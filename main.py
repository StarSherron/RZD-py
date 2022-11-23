import sys
import json
from flask import Flask, render_template, request
from flask_flatpages import pygments_style_defs
from flask_mobility import Mobility
from flask_mobility.decorators import mobile_template

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
Mobility(app)


@app.route("/", methods=['GET', 'POST'])
@mobile_template("{mobile/}index.html")
def index(template):
    if request.method == 'GET':
        return render_template(template)
    else:
        #В дальнейшем понадобится, сейчас бесполезно.
        pass


@app.route('/leisure')
def gotoleisure():
    print("leisure")
    return Null


@app.route('/charge')
def gotocharge():
    print("charge")
    return Null


@app.route('/baggage')
def gotobaggage():
    print("baggage")
    return Null


@app.route('/navigation')
def gotonavigation():
    print("navigation")
    return Null


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
