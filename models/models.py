from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base_Model = declarative_base()


class User(Base_Model):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(20))
    fullname = Column(String(40))
    password = Column(String(40))
    type = Column(String(40))
    rule = Column(String(40))

    def __repr__(self):
        return "<User (name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)


class Order(Base_Model):
    __tablename__ = 'order'

    id = Column(Integer, Sequence('order_id_seq'), primary_key=True)
    user_id = Column(String(20))
    amount = Column(String(40))
    status = Column(String(40))

    def __repr__(self):
        return "<Order (user_id='%s', amount='%s', status='%s')>" % (self.user_id, self.amount, self.status)
