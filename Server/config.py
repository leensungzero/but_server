import os
from datetime import timedelta


class Config:
    SERVICE_NAME = 'BUT'

    MYSQL_SET = {
        'user': os.getenv('MYSQL_USER', 'fast_reddit'),
        'pw': os.getenv('MYSQL_PASSWORD', 'dlstjdwpfh'),
        'host': os.getenv('MYSQL_HOST', 'onlineshop-reddit.ccxew5njw4rl.ap-northeast-2.rds.amazonaws.com'),
        'db_name': os.getenv('MYSQL_DB_NAME', 'highthon_trip')
    }

    SWAGGER = {
        'title': SERVICE_NAME,
        'specs_route': os.getenv('SWAGGER_URI', '/docs'),
        'uiversion': 3,

        'info': {
            'title': SERVICE_NAME + ' API',
            'version': '1.0',
            'description': ''
        },
        'basePath': '/',
    }

    SECRET_KEY = os.getenv('SECRET_KEY', '%nzht7dv+8bkxoe_u(7+-q_pwyb-#r%)z790si+1lh2!x4-fta')

    SWAGGER_TEMPLATE = {
        'schemes': [
            'https'
        ]
    }

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = \
        'mysql+pymysql://{user}:{pw}@{host}/{db_name}'.format(
            user=MYSQL_SET['user'],
            pw=MYSQL_SET['pw'],
            host=MYSQL_SET['host'],
            db_name=MYSQL_SET['db_name']
        )

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=365)


class DevelopmentConfig(Config):
    pass


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL', 'sqlite:///:memory:')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=10)


class ProductionConfig(Config):
    pass


config = {
    'develop': DevelopmentConfig,
    'testing': TestConfig,
    'production': ProductionConfig
}
