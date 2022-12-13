from  sqlalchemy import  Column, Integer, String, ForeignKey, Table
from  sqlalchemy.orm import relationship

from lab14.models.database import Base


association_table = Table('association', Base.metadata,
                          Column(('discipline.id'), Integer, ForeignKey('discipline.id')),
                          Column(('discipline.name'), Integer, ForeignKey('discipline.name')))
class Pulpit(Base):
    __tablename__ = "Кафедра"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    disciplines = relationship('Дисциплина', secondary=association_table, backref='discipline.name')

    def  __init__(self, name: str):
        self.name = name

    def __repr__(self):
        info: str = f'Кафедра {self.name}'
        return info

ASOIU = Pulpit("АСОИУ")
# print(repr(ASOIU))