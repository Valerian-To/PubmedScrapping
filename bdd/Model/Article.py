from ..parameter import Base
from sqlalchemy import (
    Column,
    String,
    Integer,
    BOOLEAN
)
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from .article_journal import association_table


class Article(Base):
    __tablename__ = 'articles'

    id = Column('id', Integer, primary_key=True)
    titre = Column('titre', String(255))
    auteur = Column('auteur', LONGTEXT)
    resume = Column('resume', LONGTEXT)
    motsCles = Column('mots_cles', String(255))
    citation = Column('citation', String(255))
    nbRef = Column('nb_ref', String(255))
    pmid = Column('pmid', String(255))
    doi = Column('doi', String(255))
    type = Column('type', String(255))
    isFree = Column('gratuit', BOOLEAN)
    journals = relationship('Journal', secondary=association_table, back_populates='articles')

    def __repr__(self):
        return f'<Article {self.titre}'
