from flask import jsonify
import dataprovider
import itertools

PAGE_SIZE = 5

def paginator(iterable):
    args = [iter(iterable)]*PAGE_SIZE
    return ([e for e in t if e!=None] for t in itertools.zip_longest(*args))

def list_pages():
  posts = dataprovider.get_post_ids()
  # if(len(posts)==0):
  #   return jsonify({'num-pages':0, 'pages':[]})

  page_array = list(paginator(posts))
  num_pages = len(page_array)
  return jsonify({'num_pages': num_pages, 'pages': page_array})

def page_by_num(num):
  posts = dataprovider.get_page(num, PAGE_SIZE)
  return jsonify([p.serialize() for p in posts])

def list_posts():
  posts = dataprovider.get_post_ids()
  return jsonify({"num_posts": len(posts), "posts": posts})

def post_by_id(id):
  post = dataprovider.get_post(id)
  return jsonify(post.serialize())
