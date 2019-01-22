from os import environ

class Config(object):
    """
    Common configurations
    """
    APP_SETTINGS = environ.get("APP_SETTINGS")
    EMAIL_PASSWORD = environ.get("EMAIL_PASSWORD")
    EMAIL_MAIL = environ.get("EMAIL_MAIL")
    SECRET_KEY = environ.get("SECRET_KEY")


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = True


class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False


class TestingConfig(Config):
    """
    Testing configurations
    """
    DEBUG = True


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}