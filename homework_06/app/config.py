import os

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
SQLALCHEMY_DATABASE_URI = os.getenv(
    "SQLALCHEMY_DATABASE_URI",
    f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:5432/{POSTGRES_DB}"
)


class Config:
    ENV = ""
    DEBUG = False
    TESTING = False
    SQLALCHEMY_ECHO = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SESSION_TYPE = os.getenv("SESSION_TYPE")
    SESSION_REDIS = os.getenv("CACHE_REDIS_URL")
    WTF_CSRF_TIME_LIMIT = 600


class ProductionConfig(Config):
    ENV = "production"


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    ENV = "testing"
    TESTING = True
    SQLALCHEMY_ECHO = True
