from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
import itertools

from config import Config
from models import db
from routes import init_api_routes

# Initialize Flask app and database
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
init_api_routes(app)

if __name__ == "__main__":
  print("RUNNING")
  app.run(debug=True)
