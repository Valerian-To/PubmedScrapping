"""
Module servant uniquement à lancer le script de scrapping
"""

from scrapPubMed import scrapping
from Config import configurationLog


if __name__ == '__main__':
    configurationLog()
    scrapping()
