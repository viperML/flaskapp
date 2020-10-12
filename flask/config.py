import os

class Config(object):
    UPLOAD_EXTENSIONS = ['.png', '.jpg']
    MAX_CONTENT_LENGTH = 500*1024*1024
    DROPZONE_MAX_FILE_SIZE = 500
    DROPZONE_TIMEOUT = 10*60*1000
    UPLOADED_FILEHOST_DEST = 'uploads'

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SECRET_KEY = 'a'

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@postgres:5432/users'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SESSION_COOKIE_SECURE = True
    # REMEMBER_COOKIE_SECURE = True
    # SESSION_COOKIE_HTTPONLY = True
    # REMEMBER_COOKIE_HTTPONLY = True

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@postgres:5432/users'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    #SESSION_COOKIE_SECURE = True
    #REMEMBER_COOKIE_SECURE = True
    #SESSION_COOKIE_HTTPONLY = True
    #REMEMBER_COOKIE_HTTPONLY = True
