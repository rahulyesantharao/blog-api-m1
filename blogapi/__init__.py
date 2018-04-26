from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
import itertools

from blogapi.config import ProductionConfig as Config 
from blogapi.models import db
from blogapi.routes import init_api_routes

# Initialize Flask app and database
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
init_api_routes(app)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Methods', 'GET')
  return response
