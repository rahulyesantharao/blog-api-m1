# Config files for app - should be loaded from environment variables
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY') or "Need to set an environment secret key"
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'need to set'
  SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
  SQLALCHEMY_ECHO = False
  DEBUG = False
  TESTING = False

class DevelopmentConfig(Config):
  SQLALCHEMY_ECHO = True
  DEBUG = True
  TESTING = True
