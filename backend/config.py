import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'your-openai-api-key')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwtsecretkey')


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    TESTING = True
