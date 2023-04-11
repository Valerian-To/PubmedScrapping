import logging
from datetime import datetime

def configurationLog():
    """
    Permet de configurer le système de log
    """
    date = datetime.now()
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='Log.log'
    )

    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)