from flask import Flask, request, jsonify, Response
from flask_cors import CORS

from res.src import Api, models, create_cloudflare_tunnel, openai_format
from res.typing import Dict, List, Model

import logging

# enable logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

app = Flask(__name__)
CORS(app)

# api instance
api = Api()

# constants
DEBUG: bool = False
HOST: str = "0.0.0.0"
PORT: int = 5000

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

    print(api.get_models())

    return jsonify(
        {"data": api.get_models()}), 200

# root path
@app.route("/", methods=["GET"])
def root():
    return Response("<h3>Welcome to the ChatGPT API!</h3>"), 200

if __name__ == "__main__":

    create_cloudflare_tunnel(PORT)
    app.run(debug=DEBUG, host=HOST, port=PORT)
