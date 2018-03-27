from flask import jsonify

from middleware import list_pages
from middleware import page_by_num
from middleware import list_posts
from middleware import post_by_id

# Set up Routes
def init_api_routes(app):
  if app:
    app.add_url_rule('/blog-api', 'list-routes', list_routes, methods=['GET'], defaults={'app':app})
    app.add_url_rule('/blog-api/pages', 'list-pages', list_pages, methods=['GET'])
    app.add_url_rule('/blog-api/pages/<int:num>', 'page-by-num', page_by_num, methods=['GET'])
    app.add_url_rule('/blog-api/posts', 'list-posts', list_posts, methods=['GET'])
    app.add_url_rule('/blog-api/posts/<string:id>', 'post-by-id', post_by_id, methods=['GET'])

def list_routes(app):
  result = []
  for rt in app.url_map.iter_rules():
    result.append({
      'methods': list(rt.methods),
      'route': str(rt)
    })
  return jsonify({'routes': result, 'total': len(result)})
