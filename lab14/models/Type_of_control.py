from  sqlalchemy import  Column, Integer, String, ForeignKey, Table
from  sqlalchemy.orm import relationship

from database import Base


association_table = Table('association', Base.metadata,
                          Column(('discipline.id'), Integer, ForeignKey('discipline.id')),
                          Column(('discipline.name'), Integer, ForeignKey('discipline.name')))

class Type_of_control(Base):
    __tablename__ = "Вид контроля"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    disciplines = relationship('Дисциплина', secondary=association_table, backref='discipline.name')

    def  __init__(self, name: str):
        self.name = name

    def __repr__(self):
        info: str = f'Вид контроля: {self.name}'
        return info

# DT = Type_of_control("ДТ")
# print(repr(DT))