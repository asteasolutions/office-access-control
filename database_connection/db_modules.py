# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, MetaData, Numeric, Table, Unicode
from sqlalchemy.dialects.mssql import BIT
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Card_Holder(Base):
    __tablename__ = 'Card Holder Names'
    id = Column('Card Holder ID', Integer, nullable=False, primary_key=True)
    site_id = Column('Site Name ID', Integer, nullable=False)
    last_name = Column('Last Name', Unicode(50))
    first_name = Column('First Name', Unicode(50))
    family_num = Column('Family Number', Numeric(18, 0), nullable=False)
    card_num = Column('Card Number', Numeric(18, 0), nullable=False)
    access_level = Column('Access Level', Integer, nullable=False)
    access_level_2 = Column('Access Level2', Integer, nullable=False)
    photo = Column('photo', Unicode(255))
    company_name = Column('Company Name', Unicode(100))
    display = Column('Display', BIT, nullable=False)



class Event_Names(Base):
    __tablename__ = 'Event Names'
    id = Column(Integer, primary_key=True)
    event_type = Column('Event Type', Integer, nullable=False)
    name = Column('Name', Unicode(100))
    nom = Column('Nom', Unicode(100))
    nombre = Column('Nombre', Unicode(100))


class Events(Base):
    __tablename__ = 'Events'
    id = Column('Event ID', BigInteger)
    event_type = Column('Event Type', Integer, nullable=False, primary_key=True)
    field_time = Column('Field Time', DateTime, nullable=False)
    logged_time = Column('Logged Time', DateTime, nullable=False)
    card_holder_id = Column('Card Holder ID', Integer, nullable=False)
    record_name_id = Column('Record Name ID', Integer, nullable=False)


class Record_Names(Base):
    __tablename__ = 'Record Names'
    record_name_id = Column('Record Name ID', Integer, primary_key=True)
    site_name_id = Column('Site Name ID', Integer)
    name = Column('Name', Unicode(50))
    nom = Column('Nom', Unicode(50))
    nombre = Column('Nombre', Unicode(50))
    record_type = Column('Record Type', Integer, nullable=False)
    address = Column('Address', Integer, nullable=False)
    display = Column('Display', BIT, nullable=False)


