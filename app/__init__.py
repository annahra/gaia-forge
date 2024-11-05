from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from neo4j import GraphDatabase

db = SQLAlchemy() 
neo4j_driver = GraphDatabase.driver("bolt://localhost:7687")

def create_app():
  app = Flask(__name__)
  app.config.from_object(Config)

  db.init_app(app) # initialize sql database

  from app.routes import main
  app.register_blueprint(main)

  return app
