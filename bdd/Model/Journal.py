from ..parameter import Base
from sqlalchemy import (
    Column,
    String,
    Integer
)
from sqlalchemy.orm import relationship
from .article_journal import association_table


class Journal(Base):
    __tablename__ = 'journals'

    id = Column('id', Integer, primary_key=True)
    nom = Column('nom', String(255))
    IF = Column('IF', String(255))
    articles = relationship('Article', secondary=association_table, back_populates='journals')

    def __repr__(self):
        return f'<Journal {self.nom}'
