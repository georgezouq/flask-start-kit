from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from common.config import config

engine = create_engine(
    'mysql+pymysql://' +
    config.mysql_user + ':' +
    config.mysql_pwd + '@' +
    config.mysql_host + ':' +
    config.mysql_port + '/' +
    config.mysql_db)

metadata = MetaData(engine)

# Database table structure

user = Table('user', metadata,
    Column('id', Integer,primary_key=True),
    Column('name', String(20)),
    Column('fullname', String(40)),
)

address_table = Table('address', metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', None, ForeignKey('user.id')),
    Column('email', String(128), nullable=False)
)

metadata.create_all()
