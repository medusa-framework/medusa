from config.app import AppConfig


class DevelopmentConfig(AppConfig):
    DEBUG = True


class TestingConfig(AppConfig):
    TESTING = True


class ProductionConfig(AppConfig):
    pass


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}
