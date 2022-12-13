from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///./database.db')
Base = declarative_base()

association_table = Table("association_table", Base.metadata,
                    Column("discipline_id", ForeignKey("discipline.id")),
                    Column("pulpit_id", ForeignKey("pulpit.id")),
                    Column("type_of_control_id", ForeignKey("type_of_control.id")))



class Discipline(Base):
    __tablename__ = "discipline"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    lecture = Column(Integer)
    practice = Column(Integer)
    labs= Column(Integer)

    pulpit_id = Column(Integer, ForeignKey("pulpit.id"))
    Type_of_control_id = Column(Integer, ForeignKey("type_of_control.id"))

    # children_P = relationship("Pulpit", back_populates="Discipline")
    # children_T = relationship("Type_of_control", back_populates="Discipline")


    # def  __init__(self, name: str, lecture: int, practice: int, labs: int):
    #     self.name = name
    #     self.lecture = lecture
    #     self.practice = practice
    #     self.labs = labs
    #
    # def __repr__(self):
    #     info: str = f'Дисциплина {self.name}'\
    #                     f' количество лекций: {self.lecture},'\
    #                     f' количество практических занятий: {self.practice},'\
    #                     f' количество лабораторных работ: {self.labs}'
    #     return info

class Pulpit(Base):
    __tablename__ = "pulpit"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    #discipline = relationship('Discipline', secondary=association_table, backref='discipline.name')

    def  __init__(self, name: str):
        self.name = name


class Type_of_control(Base):
    __tablename__ = "type_of_control"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    discipline_id = Column(String, ForeignKey("discipline.id"))

    # def  __init__(self, name: str):
    #     self.name = name
    #
    # def __repr__(self):
    #     info: str = f'Вид контроля: {self.name}'
    #     return info

Base.metadata.create_all(bind=engine)