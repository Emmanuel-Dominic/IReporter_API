from .config import Config,app_config
from os import environ
import psycopg2
from psycopg2.extras import RealDictCursor


class DatabaseConnection:
    def __init__(self):
        """ create tables in the PostgreSQL database"""
        if environ.get('APP_SETTINGS') == app_config['testing']:
            # self.db = 'ireporter_testing_db'
            print("connected to testing")
        elif environ.get('APP_SETTINGS') == app_config['production']:
            # self.db = 'Database'
            print("connected to production")
        elif environ.get('APP_SETTINGS') == app_config['development']:
            # self.db = 'ireporter_Database'
            print("connected to development")

        DATABASE_URL = environ.get("DATABASE_URL")
        connection = psycopg2.connect(DATABASE_URL)
        # connection = psycopg2.connect(dbname=self.db, user='postgres', password='', host='localhost', port='5432')

        connection.autocommit = True
        self.cursor = connection.cursor(cursor_factory=RealDictCursor)
        self.cursor.execute(open('sql.sql', 'r').read())
        print(self.cursor)
