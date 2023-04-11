from .enregistrement import enregistrement
from .parameter import Base, engine


def connexion(listArticle):
    """
    Ouvre une connexion à la BDD et enregistre les données
    """
    Base.metadata.create_all(engine)
    enregistrement(listArticle)

