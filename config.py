import os

class BaseConfiguration:
    DEBUG = True
    SECRET_KEY = '254HHSY18836'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfiguration(BaseConfiguration):
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DB_URL')

class DevelopmentConfiguration(BaseConfiguration):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URL')
    
class ProductionConfiguration(BaseConfiguration):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URL')

configuration = {
    'DEFAULT' : DevelopmentConfiguration,
    'TESTING' : TestingConfiguration,
    'DEVELOPMENT' : DevelopmentConfiguration,
    'PRODUCTION' : ProductionConfiguration
}