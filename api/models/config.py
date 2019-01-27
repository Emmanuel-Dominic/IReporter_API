from os import environ


class Config(object):
    """
    Common configurations
    """
    DATABASE_URL = environ.get("DATABASE_URL")
    MAIL_PASSWORD = environ.get("MAIL_PASSWORD")
    MAIL_USERNAME = environ.get("MAIL_USERNAME")
    SECRET_KEY = environ.get("SECRET_KEY")
    MAIL_SERVER = environ.get("MAIL_SERVER")
    MAIL_PORT = environ.get("MAIL_PORT")
    MAIL_USE_TLS = environ.get("MAIL_USE_TLS")
    MAIL_USE_SSL = environ.get("MAIL_USE_SSL")


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
