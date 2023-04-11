import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
load_dotenv()

loginDb = os.getenv('LOGIN_DB')
passwordDb = os.getenv('PASSWORD_DB')
Base = declarative_base()
engine = create_engine('mysql+mysqlconnector://'+loginDb+':'+passwordDb+'@localhost/pubmed', echo=True)
Session = sessionmaker()
