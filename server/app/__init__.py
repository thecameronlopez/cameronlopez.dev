import os
from flask import Flask
from config import Config
from .extensions import (
    db,
    migrate,
    cors,
    login_manager,
    bcrypt    
)
from app.models import User

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    #extension init
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    
    #import blueprint
    from .api import api as api_bp
    app.register_blueprint(api_bp)
    
    
    #load user
    @login_manager.user_loader
    def load_user(id):
        return db.session.get(User, id)
    
    return app