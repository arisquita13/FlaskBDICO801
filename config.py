import os 
from sqlalchemy import create_engine

class Config(object):
    SECRET_KEY = "claveSecreta"
    SSESSION_COOKIE_SECURE = False
    

    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI ='mysql+pymysql://:Ariadna:root@localhost:3306/ico801'
    SQLALCHEMY_TRACK_MODIFICATIONS = False