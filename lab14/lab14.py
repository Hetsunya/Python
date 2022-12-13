import models
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine

engine = create_engine('sqlite:///./database.db')
session = Session(bind='sqlite:///./database.db')


def create_database(load_fake_data: bool = True):
    if load_fake_data:
        _load_fake_data()


def _load_fake_data(value):
    disciplines_names = ['Математика', 'Программирование', 'Философствуем', 'Алгоритмы и структуры данных',
                         'Линейная алгебра', 'Мат. статистика', 'Физкультура']

    # pulpit1 = Pulpit(name='ASOIU')
    pulpit = models.Pulpit(name=value['ASOIU'])
    value.append(pulpit)
    session.add(pulpit)
    # pulpit2 = Pulpit(name='IVT')
    # Session.add(pulpit1)
    # Session.add(pulpit2)
    #
    # for d in disciplines_names:
    #     Session.add(d)

    # discipline_list = [pulpit1, pulpit2]
    session.commit()
    session.close()

# _load_fake_data()
value = list()
create_database(value)