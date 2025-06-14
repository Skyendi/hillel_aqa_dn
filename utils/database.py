import logging

from dotenv import load_dotenv
load_dotenv()
import psycopg2
from psycopg2 import Error
import os


class PostresDB:
    def __init__(self):
        self.dbname = os.getenv("db_name")
        self.user = os.getenv("user")
        self.password = os.getenv("password")
        self.host = os.getenv("host")
        self.port = os.getenv("port")
        self._connect()

    def _connect(self):
        try:
            self.__connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.__connection.autocommit = True
            self.__cursor = self.__connection.cursor()
            print("Connected to the database successfully!")
        except Error as e:
            print(f"[DB CONNECTION ERROR] {e}")
            self.__connection = None
            self.__cursor = None

    @property
    def cursor(self):
        return self.__cursor

    @property
    def conn(self):
        return self.__connection

    def select(self, query: str) -> list[tuple] | list[None]:
        logging.info(f"Making select query\n{query}")
        if not self.cursor:
            raise ConnectionError("No database connection.")
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def mutation(self, query: str) -> None:
        logging.info(f"Making mutation:\n{query}")
        if not self.cursor:
            raise ConnectionError("No database connection.")
        self.cursor.execute(query)

    def close(self):
        if self.__cursor:
            self.__cursor.close()
        if self.__connection:
            self.__connection.close()
        print("Database connection closed.")

    def __del__(self):
        try:
            self.close()
        except Exception as e:
            print(f"[DEL ERROR] {e}")
