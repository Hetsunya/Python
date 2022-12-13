from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
import sqlalchemy as db
engine = create_engine('sqlite:///./database.db')
Base = declarative_base()

association_table = Table(
    "association_table",
    Base.metadata,
    Column("content_id", ForeignKey("content.id")),
    Column("sections_id", ForeignKey("sections.id")),
)


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    nickname = Column(String)
    children = relationship("Content")


class Section(Base):
    __tablename__ = 'sections'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Content(Base):
    __tablename__ = 'content'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    annotation = Column(String)
    contents = Column(String)
    authors_id = Column(Integer, ForeignKey("authors.id"))
    sections = relationship("Section", secondary="association_table", viewonly=True)



Base.metadata.create_all(bind=engine)