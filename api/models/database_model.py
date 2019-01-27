from os import environ

import psycopg2
from psycopg2.extras import RealDictCursor

from .config import app_config


class DatabaseConnection:
    def __init__(self):
        """ create tables in the PostgreSQL database"""
        if environ.get('APP_SETTINGS') == app_config['testing']:
            print("connected to testing")
        elif environ.get('APP_SETTINGS') == app_config['production']:
            print("connected to production")
        elif environ.get('APP_SETTINGS') == app_config['development']:
            print("connected to development")

        DATABASE_URL = environ.get("DATABASE_URL")
        connection = psycopg2.connect(DATABASE_URL)

        connection.autocommit = True
        self.cursor = connection.cursor(cursor_factory=RealDictCursor)
        self.cursor.execute(open('sql.sql', 'r').read())
        print(self.cursor)
