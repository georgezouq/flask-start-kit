from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import db_path
from models import Base_Model

engine = create_engine(db_path)

DB_Session = sessionmaker(bind=engine)
session = DB_Session()


def init_tables():
    Base_Model.metadata.create_all(engine)