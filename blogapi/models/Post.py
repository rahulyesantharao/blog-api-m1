# pylint: disable=E1101
from blogapi.models import db

class Post(db.Model):
  __tablename__ = 'posts'
  id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
  post_id = db.Column('post_id', db.String(50), index=True, nullable=False)
  post_date = db.Column('date', db.Date, nullable=False)
  post_title = db.Column('title', db.String(200), nullable=False)
  post_md = db.Column('md', db.Text, nullable=False)
  post_html = db.Column('html', db.Text, nullable=False)
  post_author = db.Column('author_id', db.Integer, db.ForeignKey('authors.id'), nullable=False)
  author = db.relationship("Author")

  def serialize(self):
    return {
      "post_id": self.post_id,
      "post_date": self.post_date,
      "post_title": self.post_title,
      "post_html": self.post_html,
      "author": self.author.serialize()
    }
