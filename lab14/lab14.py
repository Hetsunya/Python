from faker import Faker

from database import create_db
from models import Discipline, Pulpit, Type_of_control

from models import Session



def create_database(load_fake_data: bool = True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session: Session):
    disciplines_names = ['Математика', 'Программирование', 'Философствуем за кружечкой пенного',
                                 'Алгоритмы и структуры данных', 'Линейная алгебра', 'Мат. статистика',
                                 'Физкультура']
    pulpit1 = Pulpit(pulpit_name='ASOIU')
    pulpit2 = Pulpit(pulpit_name='ISIT')
    session.add(pulpit1)
    session.add(pulpit2)

    for key, it in enumerate(disciplines_names):
        lesson = Discipline(lesson_title=it)
        lesson.groups.append(pulpit1)
        if key % 2 == 0:
            lesson.groups.append(pulpit2)
        session.add(lesson)

    faker = Faker('ru_RU')
    discipline_list = [pulpit1, pulpit2]
    session.commit()
    session.close()