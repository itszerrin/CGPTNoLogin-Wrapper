from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from flask_cloudflared import run_with_cloudflared

from res.src.Api import Api
from res.src.Models import models
from res.typing import Dict, List, Model
from res.src.format import openai_format

import logging

# enable logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

app = Flask(__name__)
CORS(app)

# api instance
api = Api()

# chatting route
@app.route("/chat/completions", methods=["POST"])
def chat():
    
        # get the request data
        data = request.json
    
        # get the messages from the request data
        messages: List[Dict[str, str]] = data["messages"]
    
        # get the model from the request data
        model: Model = data.get("model", "gpt-3.5-turbo")

        # try getting temperature. default = 0.7
        temperature: float = data.get("temperature", 0.7)

        # compile model to Model object
        model = models[model]

        # chat
        response = api.chat(messages, model, temperature=temperature)

        # return the response
        return jsonify(openai_format(response, model["id"])), 200

# get models
@app.route("/models", methods=["GET"])
def get_models():

    return jsonify(
        {"data": api.get_models()}), 200

if __name__ == "__main__":

    run_with_cloudflared(app)
    app.run(debug=False, host="0.0.0.0", port=5000)