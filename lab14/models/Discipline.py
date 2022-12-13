from  sqlalchemy import  Column, Integer, String, ForeignKey

from database import Base

class Discipline(Base):
    __tablename__ = "Дисциплина"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    lecture = Column(Integer)
    practice = Column(Integer)
    labs= Column(Integer)
    ToC = Column(Integer, ForeignKey("Type_of_control.id"))

    def  __init__(self, name: str, lecture: int, practice: int, labs: int):
        self.name = name
        self.lecture = lecture
        self.practice = practice
        self.labs = labs

    def __repr__(self):
        info: str = f'Дисциплина {self.name}'\
                        f' количество лекций: {self.lecture},'\
                        f' количество практических занятий: {self.practice},'\
                        f' количество лабораторных работ: {self.labs}'
        return info

# OP =Discipline("Основы программирования", 72, 72, 15)
# print(repr(OP))

