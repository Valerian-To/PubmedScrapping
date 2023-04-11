from sqlalchemy import(
    Table,
    Column,
    Integer,
    ForeignKey
)
from ..parameter import Base
association_table = Table(
    'articles_journals',
    Base.metadata,
    Column('article_id', ForeignKey('articles.id')),
    Column('journal_id', ForeignKey('journals.id'))
)
