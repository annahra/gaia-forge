import os

class Config:
  # SQL db config
  SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI","postgresql://user:password@localhost/mydb")
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  