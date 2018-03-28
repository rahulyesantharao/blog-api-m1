from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
import itertools

from blogapi.config import DevelopmentConfig
from blogapi.models import db
from blogapi.routes import init_api_routes

# Initialize Flask app and database
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
init_api_routes(app)

