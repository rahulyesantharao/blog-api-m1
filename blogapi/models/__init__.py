from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from blogapi.models.Author import Author
from blogapi.models.Post import Post
__all__ = ['Author', 'Post']
