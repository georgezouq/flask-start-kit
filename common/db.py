from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import db_config
from models import Base_Model

engine = create_engine(
    'mysql+pymysql://' +
    db_config['mysql_user'] + ':' +
    db_config['mysql_pwd'] + '@' +
    db_config['mysql_host'] + ':' +
    db_config['mysql_port'] + '/' +
    db_config['mysql_db'])

DB_Session = sessionmaker(bind=engine)
session = DB_Session()


def init_tables():
    print('Ready to init tables')
    Base_Model.metadata.create_all(engine)