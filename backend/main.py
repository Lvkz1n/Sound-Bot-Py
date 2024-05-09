from flask_restx import  Api
from flask_cors import CORS
from flask import Flask, jsonify, make_response

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["use_reloader"] = True
api_prefix_url = "/api/core"

CORS(Api)



