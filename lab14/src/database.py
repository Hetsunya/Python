from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from . import models

engine = create_engine('sqlite:///database.db')
session = Session(bind=engine)

# https://qna.habr.com/q/234261

def add_type_of_control(name):
    name_toc = session.query(models.Type_of_control).filter(models.Type_of_control == name)

    if name_toc.first() > 0:
        return print("Данный вид контроля уже есть в базе данных")
    else:
        new_type = models.Type_of_control(
            name=name
            )


    # for toc in
    session.add(new_type)
    session.commit()

def add_pulpit(name):
     new_pulpit = models.Pulpit(
        name=name
    )

     session.add(new_pulpit)
     session.commit()

def add_discipline(name, lecture, practice, labs, pulpit_id):
     pulpits = session.query(models.Pulpit).filter(models.Pulpit.id == pulpit_id)

     new_discipline = models.Discipline(
         name=name,
         lecture=lecture,
         practice=practice,
         labs=labs,
         pulpit_id=pulpit_id,
     )

     if pulpits:
         session.add(new_discipline)
         session.commit()
     else:
         return print(f'Номер кафедры {pulpit_id} не найден')


    # def append_discipline_to_pulpit(, id_discipline, id_pulpit):
    #     if not id_pulpit:
    #         return
    #
    #     pulpits = session.query(models.Pulpit).filter(models.Pulpit.id.in_(id_pulpit))
    #     assert pulpits.count(), f"id_puplit {id_pulpit} not found"
    #
    #     disciplines = session.query(models.Discipline).filter(models.Discipline.id == id_discipline)
    #     assert disciplines.count(), f"id_disciplin <{id_discipline}> not found"
    #     discipline = disciplines.first()
    #
    #     for feed in pulpits.all():
    #         disciplines.disciplin.append(feed)
    #
    #         session.add(feed)
    #
    #     session.add(discipline)
    #     session.commit()

def all_disciplines():
    result = {}

    disciplines = session.query(models.Discipline).all()

    pulpits = session.query(models.Pulpit).all()

    for discipline in disciplines:
        result[str(discipline.id)] = {
                "name": discipline.name,
                "lecture": discipline.lecture,
                "practice": discipline.practice,
                "labs": discipline.labs,
                "pulpit_name": discipline.pulpit_id
            }

    return result

def all_pulpit():
    result = {}
    pulpits = session.query(models.Pulpit).all()

    count = 0
    disciplines = session.query(models.Discipline).all()


    for pulpit in pulpits:
        for discipline in disciplines:
            if discipline.pulpit_id == pulpit.id:
                count += 1

        result[str(pulpit.id)] = {
                "name": pulpit.name,
                "count_disciplines": count
            }
        count = 0


    return result

    # def all_types_of_control():
    #     types = session.query(models.Type_of_control).all()
    #
    #     return {str(i.id): i.title for i in types}
