from flask import render_template, request, redirect, url_for
from . import blog_bp

@blog_bp.route('/posts')
def posts():
    # Example route that renders a template
    return render_template('posts.html')

@blog_bp.route('/post/<int:post_id>')
def post(post_id):
    # Example route to view a specific post
    return f'Post {post_id}'
