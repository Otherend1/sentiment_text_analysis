import os
import sys
import time
    
import json
import urllib
import requests

sys.path.append("../python")

from flask import Flask, request, jsonify,send_from_directory, url_for
from flask.templating import render_template
from flask_basicauth import BasicAuth

from sentiment_text_analysis.settings import settings

back_settings = settings["demos"]["sentiment_text_analysis"]["back"]
front_settings = settings["demos"]["sentiment_text_analysis"]["front"]["predict"]

BACK_URL = "http://"+back_settings["ip"]+":"+str(back_settings["port"])

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = "ANEODATA"
app.config['BASIC_AUTH_PASSWORD'] = "aneodata"
app.config['BASIC_AUTH_FORCE'] = True
app.config['STATIC_FOLDER'] = os.path.abspath("./static/")

app.secret_key = str(time.time())

basic_auth = BasicAuth(app)


@app.route('/', methods=['GET'])
@basic_auth.required
def index():
    """Main page. Do not need to manipulate templating but shown as an example."""
    args = {}
    
    return render_template('index.html', **args)

@app.route('/send_sentence', methods=['POST', 'GET'])
@basic_auth.required
def send_sentence():
    print("*************************START PROCESSING****************************", file=sys.stderr)
    sentence = request.form["sentence"]
    payload = {"sentence": sentence}
    r = requests.post(BACK_URL + "/predict", data=json.dumps(payload))
    res = r.json()

    return jsonify(res) 


if __name__ == '__main__':
    app.run(debug=False, host=front_settings["ip"], port=front_settings["port"], ssl_context=('ssl_context/cert.pem', 'ssl_context/key.pem'))
