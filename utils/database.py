from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils.functions import database_exists, create_database

from utils.definitions import MySQL


def connect(db_name):
    connection_string = "mysql://{username}:{password}@{host}:{port}/{database}".format(username=MySQL.username,
                                                                                        password=MySQL.password,
                                                                                        host=MySQL.host,
                                                                                        port=MySQL.port,
                                                                                        database=db_name)
    if not database_exists(connection_string):
        create_database(connection_string)
    db_conn = create_engine(connection_string)
    return db_conn


def create_session(db_name):
    return sessionmaker(bind=connect(db_name))
