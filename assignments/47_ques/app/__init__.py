from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Import and register the blueprint
    from .blog import blog_bp
    app.register_blueprint(blog_bp, url_prefix='/blog')
    
    return app
