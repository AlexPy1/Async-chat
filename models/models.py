import sqlite3
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import mapper, declarative_base

engine = create_engine('sqlite:///server_db.sqlite', echo=True)

Base = declarative_base()



class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    login = Column(String)
    info = Column(String)

    def __init__(self, login, info):
        self.login = login
        self.info = info

    def __repr__(self):
        return "<Client('%s','%s')>" % (self.login, self.info)


class HistoryClient(Base):
    __tablename__ = 'history_client'
    id = Column(Integer, primary_key=True)
    entry_time = Column(String)
    ip = Column(String)
    client_id = Column(Integer, ForeignKey('clients.id'))

    def __init__(self, entry_time, ip):
        self.entry_time = entry_time
        self.ip = ip

    def __repr__(self):
        return "<Last online '%s', User_ip '%s'>" % (self.entry_time, self.ip)


class ContactList(Base):
    __tablename__ = 'contact_list'
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.id'))
    owner_id = Column(Integer, ForeignKey('clients.id'))


    def __init__(self, owner_id, client_id):
        self.owner_id = owner_id
        self.client_id = client_id

    def __repr__(self):
        return "<Owner_id: '%d', client_id: '%d')>" % (self.owner_id, self.client_id)


clients_table = Client.__table__
history_client_table = HistoryClient.__table__
contact_list_table = ContactList.__table__

print(clients_table, history_client_table, contact_list_table)

Base.metadata.create_all(engine)