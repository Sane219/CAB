from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from .routes.api import api_bp

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    mongo.init_app(app)
    CORS(app)
    
    app.register_blueprint(api_bp, url_prefix='/api')
    
    return app