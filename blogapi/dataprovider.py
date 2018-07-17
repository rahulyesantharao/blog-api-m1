# pylint: disable=E1101
from blogapi.models import Post
from flask import abort

def get_post_ids():
  ret = Post.query.with_entities(Post.post_id).all()
  return [r[0] for r in ret]

def get_post(id):
  post = Post.query.filter_by(post_id=id).first_or_404()
  return post

def get_page(num, n):
  if(num<1):
    abort(404)
  posts = Post.query.order_by(Post.post_date.desc()).offset((num-1)*n).limit(n).all()
  if(len(posts) == 0):
    abort(404)
  #posts = Post.query.paginate(num, n).items
  return posts
