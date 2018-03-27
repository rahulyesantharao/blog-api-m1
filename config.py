# Config files for app - should be loaded from environment variables
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY') or "Need to set an environment secret key"
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'databaseuri'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_ECHO = True # Set to False for production
