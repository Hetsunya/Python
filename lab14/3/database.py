# https://youtu.be/70mNRClYJko
from  sqlalchemy.orm import declarative_base, sessionmaker
from  sqlalchemy import Column, String, DateTime, Integer, create_engine
from  datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
DATABASE_NAME = 'application.sqlite'

#connection_string = "sqlite:///" + os.path.join(BASE_DIR, DATABASE_NAME)

#engine = create_engine(connection_string)
engine = create_engine(f'sqlite:///{DATABASE_NAME}')
Session = sessionmaker(bind=engine)

Base = declarative_base()

def create_db():
    Base.metadata.create_all(bind=engine)