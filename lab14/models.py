from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///./database.db')
Base = declarative_base()

association_table = Table("association_table", Base.metadata,
                    Column("discipline_id", Integer, ForeignKey("discipline.id")),
                    Column("pulpit_id", Integer, ForeignKey("pulpit.id")),
                    Column("type_of_control_id", Integer, ForeignKey("type_of_control.id")))

class Discipline(Base):
    __tablename__ = "discipline"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    lecture = Column(Integer)
    practice = Column(Integer)
    labs= Column(Integer)

    pulpit_id = Column(Integer, ForeignKey("pulpit.id"))
    Type_of_control_id = Column(Integer, ForeignKey("type_of_control.id"))

class Pulpit(Base):
    __tablename__ = "pulpit"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    discipline = relationship('Discipline', secondary=association_table, backref='discipline.name')

class Type_of_control(Base):
    __tablename__ = "type_of_control"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    discipline_id = Column(String, ForeignKey("discipline.id"))

Base.metadata.create_all(bind=engine)