# pylint: disable=E1101
from blogapi.models import db

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
