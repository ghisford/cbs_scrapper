from distutils.debug import DEBUG


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost:3306/nzima_flask'
    SECRET_KEY = 'NEWSSTUFF'

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class TestConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False

    
app_config = {'development':DevelopmentConfig,
                'production':ProductionConfig,
                'testing':TestConfig,
            }