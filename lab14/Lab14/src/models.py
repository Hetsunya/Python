from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float, create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, Session

Base = declarative_base()
engine = create_engine('sqlite:///database.db')


association_table = Table(
    'association_table', Base.metadata,
    Column("discipline_id", Integer(), ForeignKey("discipline.id")),
    Column("pulpit_id", Integer(), ForeignKey("pulpit.id")),
    Column("type_of_control_id", Integer(), ForeignKey("type_of_control.id"))
)


class Discipline(Base):
    __tablename__ = "discipline"

    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    lecture = Column(Integer)
    practice = Column(Integer)
    labs = Column(Integer)
    pulpit_id = Column(Integer, ForeignKey("pulpit.id"))

    # def __init__(self, name, lecture, practice, labs, pulpit_id):
    #     self.name = name
    #     self.lecture = lecture
    #     self.practice = practice
    #     self.labs = labs
    #     self.pulpit_id = pulpit_id


class Pulpit(Base):
    __tablename__ = "pulpit"

    id = Column(Integer, primary_key=True)
    name = Column(String(10))

    def __init__(self, name):
        self.name = name

    disciplines = relationship('Discipline', backref='pulpit')
    # disciplines = Column(Integer, ForeignKey("discipline.id"))


class Type_of_control(Base):
    __tablename__ = "type_of_control"

    id = Column(Integer, primary_key=True)
    name = Column(String(15))


Base.metadata.create_all(bind=engine)

# ASOIU = Pulpit('ASOIU')
# OP = Discipline("OP", 16, 16, 15, 9865)
#
#
# # print(ASOIU.name)
# print(OP.pulpit_id)
#
# sessoin = Session(bind=engine)
#
# # sessoin.add(ISIT)
# sessoin.add(OP)
# sessoin.commit()