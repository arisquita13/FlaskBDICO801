import os 
from sqlalchemy import create_engine

class Config(object):
    SECRET_KEY = "claveSecreta"
    SSESSION_COOKIE_SECURE = False
    

    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI ='mysql+pymysql://ariadna:root@3306/ICO801'
    SQLALCHEMY_TRACK_MODIFICATIONS = False