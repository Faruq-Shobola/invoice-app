from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config


db = SQLAlchemy()

def create_app():

  app = Flask(__name__)
  app.config.from_object(Config)
  
  
  from .auth.routes import auth
  
  app.register_blueprint(auth)
  
  db.init_app(app)
  
  
  
  with app.app_context():
    db.create_all()
  
  return app