from datetime import date

import sqlalchemy.engine
from sqlalchemy.orm import Session

from . import models


class DataBase:
    def __init__(self, engine: sqlalchemy.engine.Engine):
        self.engine = engine
        self.session = Session(bind=engine)

    def add_type_of_control(self, type: str):
        new_type = models.Type_of_control(
            title=type
        )

        self.session.add(new_type)
        self.session.commit()

    def add_pulpit(self, name):
        new_pulpit = models.Pulpit(
            name=name
        )

        self.session.add(new_pulpit)
        self.session.commit()

    def add_discipline(self, name, lecture, practice, labs, pulpit_id):
        pulpits = self.session.query(models.Pulpit).filter(models.Pulpit.id == pulpit_id)

        if pulpits:
            new_discipline = models.Discipline(
                name=name,
                lecture=lecture,
                practice=practice,
                labs=labs,
                pulpit_id=pulpit_id,
            )

            self.session.add(new_discipline)
            self.session.commit()
        else:
            return print(f'Номер кафедры {pulpit_id} не найден')


    # def append_discipline_to_pulpit(self, id_discipline, id_pulpit):
    #     if not id_pulpit:
    #         return
    #
    #     pulpits = self.session.query(models.Pulpit).filter(models.Pulpit.id.in_(id_pulpit))
    #     assert pulpits.count(), f"id_puplit {id_pulpit} not found"
    #
    #     disciplines = self.session.query(models.Discipline).filter(models.Discipline.id == id_discipline)
    #     assert disciplines.count(), f"id_disciplin <{id_discipline}> not found"
    #     discipline = disciplines.first()
    #
    #     for feed in pulpits.all():
    #         disciplines.disciplin.append(feed)
    #
    #         self.session.add(feed)
    #
    #     self.session.add(discipline)
    #     self.session.commit()

    def all_disciplines(self):
        result = {}

        disciplines = self.session.query(models.Discipline).all()

        pulpits = self.session.query(models.Pulpit).all()

        for discipline in disciplines:
            result[str(discipline.id)] = {
                "name": discipline.name,
                "lecture": discipline.lecture,
                "practice": discipline.practice,
                "labs": discipline.labs,
                "pulpit_name": discipline.pulpit_id
            }

        return result

    def all_pulpit(self):
        result = {}
        pulpits = self.session.query(models.Pulpit).all()

        count = 0
        disciplines = self.session.query(models.Discipline).all()


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

    # def all_types_of_control(self):
    #     types = self.session.query(models.Type_of_control).all()
    #
    #     return {str(i.id): i.title for i in types}


