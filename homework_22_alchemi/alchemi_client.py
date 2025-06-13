from sqlalchemy import create_engine, func, select
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import logging
#logging.basicConfig(level=logging.DEBUG)
import os
load_dotenv()





class SQLAlchemyClient:
    def __init__(self, db_url: str):
        self.db_url = db_url
        self.__engine = self.__create_engine()
        self.__session = self.__create_session()

    @property
    def session(self):
        return self.__session

    def __create_engine(self):
        #logging.info(f"Creating engine for {self.db_url}...")
        return create_engine(self.db_url)

    def __create_session(self):
        #logging.info(f"Creating session for {self.db_url}...")
        session = sessionmaker(bind=self.__engine)
        return session()

    def create_table(self, table_obj):
        #logging.info(f"Creating table {table_obj.__tablename__}...")
        table_obj.metadata.create_all(self.__engine)

    def close_connection(self):
        #logging.info("Connection closed")
        self.__session.close()