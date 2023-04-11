from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()
engine = create_engine('mysql+mysqlconnector://root:root@localhost/pubmed', echo=True)
Session = sessionmaker()
