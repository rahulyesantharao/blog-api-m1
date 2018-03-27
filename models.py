# pylint: disable=E1101
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Post(db.Model):
  __tablename__ = 'posts'
  id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
  post_id = db.Column('post-id', db.String(50), index=True, nullable=False)
  post_date = db.Column('post-date', db.Date, nullable=False)
  post_title = db.Column('post-title', db.String(200), nullable=False)
  post_md = db.Column('post-md', db.Text, nullable=False)
  post_html = db.Column('post-html', db.Text, nullable=False)
  post_author = db.Column('post-author-id', db.Integer, db.ForeignKey('authors.id'), nullable=False)
  author = db.relationship("Author")

  def serialize(self):
    return {
      "post_id": self.post_id,
      "post_date": self.post_date,
      "post_title": self.post_title,
      "post_html": self.post_html,
      "author": self.author.serialize()
    }

class Author(db.Model):
  __tablename__ = 'authors'
  id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
  name = db.Column(db.String(45), nullable=False)
  location = db.Column(db.String(45), nullable=False)
  description = db.Column(db.String(45), nullable=False)

  def serialize(self):
    return {
      "name": self.name,
      "location": self.location,
      "description": self.description
    }
