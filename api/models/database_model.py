from .config import Config
from os import environ
import psycopg2
from psycopg2.extras import RealDictCursor

class DatabaseConnection:

    def __init__(self):
        """ create tables in the PostgreSQL database"""
        if environ.get('APP_SETTINGS') == 'testing':
            self.db = 'ireporter_testing_db'
            print("connected to test_db")
        elif environ.get('APP_SETTINGS') == 'production':
            self.db = 'test_db'
            print("connected to test_db")
        else:
            self.db = 'ireporter_Database'
            print("connected to ireporter_Database")

        connection = psycopg2.connect(dbname=self.db, user='postgres', password='', host='localhost', port='5432')

        connection.autocommit = True
        self.cursor = connection.cursor(cursor_factory=RealDictCursor)
        self.cursor.execute(open('sql.sql','r').read())
        print(self.cursor)