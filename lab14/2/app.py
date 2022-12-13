import PySimpleGUI as sg
import models
from sqlalchemy.orm import sessionmaker, Session
import sqlalchemy as db

sg.theme('DarkAmber')
engine = db.create_engine('sqlite:///./database.db')
Session = sessionmaker(bind=engine)
session = Session()

layout = [[sg.Text('Автор'), sg.Combo(session.query(models.Author.nickname).all(), key='au', enable_events=True, size=25), sg.Text('email'), sg.InputText(size=20, key='email')],
          [sg.Text('Раздел'), sg.Combo(session.query(models.Section.name).all(), key='sec', enable_events=True, size=25)],
          [sg.Text('Название контента'), sg.InputText(size=20), sg.Text('Аннотация'), sg.InputText(size=20)],
          [sg.Text('Содержимое'), sg.InputText(size=58)],
          [sg.Button('Добавить запись')],
          [sg.Button('Просмотреть весь контент'), sg.Button('Просмотреть всех авторов')],
          [sg.Text('Не все поля заполнены', text_color=sg.GREENS[0], visible=False, key='er')]]

window = sg.Window('work with db', layout)



def add_note(val):
    session = Session()
    author = models.Author(nickname=val['au'][0], email=val['email']) if not len(session.query(models.Author).filter_by(nickname=val['au'][0]).all()) \
        else session.query(models.Author).filter_by(nickname=val['au'][0]).first()
    sections = models.Section(name=val['sec'][0]) if not len(session.query(models.Section).filter_by(name=val['sec'][0]).all()) \
        else session.query(models.Section).filter_by(name=val['sec'][0]).first()
    content = models.Content(name=val[0], annotation=val[1], contents=val[2])
    author.children.append(content)
    content.sections.append(sections)
    session.add(author)
    session.add(sections)
    session.add(content)
    session.commit()
    window['au'].update(value='', values=session.query(models.Author.nickname).all())
    window['sec'].update(value='', values=session.query(models.Section.name).all())

def add_author(val):
    session = Session()
    author = models.Author(nickname=val['au'], email=val['email']) if not len(session.query(models.Author).filter_by(nickname=val['au']).all()) \
        else session.query(models.Author).filter_by(nickname=val['au']).first()
    session.add(author)
    session.commit()
    window['au'].update(value='', values=session.query(models.Author.nickname).all())

def add_section(val):
    session = Session()
    sections = models.Section(name=val['sec']) if not len(session.query(models.Section).filter_by(name=val['sec']).all()) \
        else session.query(models.Section).filter_by(name=val['sec']).first()
    if val[0] != '' and val[1] != '' and val[2] != '':
        content = models.Content(name=val[0], annotation=val[1], contents=val[2])
        content.sections.append(sections)
        session.add(content)
    session.add(sections)
    session.commit()
    window['sec'].update(value='', values=session.query(models.Section.name).all())

def all_authors():
    session = Session()
    nicknames = session.query(models.Author.nickname).all()
    emails = session.query(models.Author.email).all()
    res = []
    for id in session.query(models.Author.id).all():
        count_of_posts = session.query(models.Content.authors_id).filter_by(authors_id=id[0]).all()
        res.append(len(count_of_posts))
    for i in range(len(nicknames)):
        print('Author: ' + nicknames[i][0] + ' | email: ' + emails[i][0] + ' | count of posts: ' + str(res[i]))


def all_content():
    session = Session()
    names = session.query(models.Content.name).all()
    annotations = session.query(models.Content.annotation).all()
    ids = session.query(models.Content.authors_id).all()
    nicknames = []
    for id in ids:
        nicknames.append(session.query(models.Author.nickname).filter_by(id=id[0]).all())
    for nick in nicknames:
        if not len(nick):
            nicknames.remove(nick)
    sections = session.query(models.Section.name).all()
    for i in range(len(names)):
        print('Content: ' + names[i][0] + ' | section: ' + sections[i][0] + ' | author: ' +
              nicknames[i][0][0] + ' | annotation: ' + annotations[i][0])


def set_email(val):
    session = Session()
    window.Element('email').Update(session.query(models.Author.email).filter_by(nickname=val['au'][0]).first())

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Quit':
        break
    if event == 'Добавить запись':
        if values['au'] != '' and values['email'] != '' and values['sec'] != '' \
                and values[0] != '' and values[1] != '' and values[2] != '':
            add_note(values)
        elif values['au'] != '' and values['email'] != '' and values['sec'] == '':
            add_author(values)
        elif values['au'] == '' and values['email'] == '' and values['sec'] != '':
            add_section(values)
        else:
            window.Element('er').Update(visible=True)
    if event == 'Просмотреть всех авторов':
        all_authors()
    if event == 'au':
        set_email(values)
    elif event == 'Просмотреть весь контент':
        all_content()