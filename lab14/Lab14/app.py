from sqlalchemy import create_engine

from src import database

engine = create_engine('sqlite:///database.db')
db = database.DataBase(engine)

print(
    """
____СПИСОК КОМАНД____
<Создание новых записей>
    1. Дисциплина
    2. Добавить кафедру
    3. Добавить животное

<Выборка данных>
    4. Все дисциплины
    5. Все кафедры

<Прочее>
    0. Выход
"""
)
while True:
    req = input("\nВыбор действия: ")

    if req == "1":
        name = input("  Название: ")
        lecture = input("  Лекций: ")
        practice = input("  Практики: ")
        labs = input("  Лаб: ")
        pulpit_id = input(" Кафедра  ")

        db.add_discipline(name, lecture, practice, labs, pulpit_id)

    elif req == "2":
        name = input("  Название кафедры: ")

        db.add_pulpit(name)
    #
    # elif req == "3":
    #     kinds = db.all_types_of_control()
    #
    #     if not kinds:
    #         print("  Перед добавление животного, сначала добавьте хотя бы один вид")
    #         continue
    #
    #     animal_name = input("  Кличка: ")
    #
    #     date_of_birth = input("  Дата рождения (YYYY-MM-DD): ")
    #     while True:
    #         try:
    #             date_of_birth = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d")
    #             break
    #         except ValueError:
    #             date_of_birth = input("  Введите корректную дату в формате YYYY-MM-DD: ")
    #
    #     gender = input("  Пол: ")
    #
    #     print("  Выберите вид животного из списка:")
    #     for kind_id, title in kinds.items():
    #         print(f"    {kind_id} - {title}")
    #
    #     kind_animal_id = input("  Номер вида: ")
    #     while kind_animal_id not in kinds:
    #         kind_animal_id = input("  Укажите номер из списка выше: ")
    #
    #     db.add_animal(animal_name, date_of_birth, gender, kind_animal_id)

    elif req == "4":
        disciplines = db.all_disciplines()

        if not disciplines:
            print("  Пока пусто")

        for id_discipline, data in disciplines.items():
            print(f"  {id_discipline} ")
            print(f"    Название: {data['name']}")
            print(f"    Лекций: {data['lecture']}")
            print(f"    Практики: {data['practice']}")
            print(f"    Лабораторные: {data['labs']}")
            print(f"    Кафедра: {data['pulpit_name']}")

    elif req == "5":
        pulpits = db.all_pulpit()

        if not pulpits:
            print("  Пока пусто")

        for id_pulpit, data in pulpits.items():
            print(f"  {id_pulpit}.  ")
            print(f"  {data['name']}, Количество дисциплин: {data['count_disciplines']} ")

    else:
        print("Введена неверная команда")
