import os
import sys
import time

sys.path.append("../../../python/")

from flask import Flask, request, abort, jsonify
from joblib import Parallel, delayed

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sentiment_text_analysis.settings import settings

back_settings = settings["demos"]["sentiment_text_analysis"]["back"]

# instantiate flask app
app = Flask(__name__)


# instantiate sentiment analysis model
sentiment_analyzer = SentimentIntensityAnalyzer()

@app.route("/predict", methods=['POST'])
def predict():
    payload = request.get_json(force=True, silent=True)
    sentence = payload["sentence"]

    try: 
        compound = sentiment_analyzer.polarity_scores(sentence)["compound"]
        min_, max_ = -1, 1
        sentiment_intensity = (min_ - compound) / (min_ - max_)
        error_msg = ""
    except:
        sentiment_intensity = None
        error_msg = "error - could not analyze sentence" 

    result = {
        "sentiment_intensity": sentiment_intensity,
        "error_msg": error_msg
    }
    
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=False, host=back_settings["ip"], port=back_settings["port"])
