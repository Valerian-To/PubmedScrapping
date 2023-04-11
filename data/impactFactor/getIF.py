"""
Module permettant la recuperation de l'impact factor d'un article
"""
from bs4 import BeautifulSoup
import requests


def getIF(articleDetail):
    """
    Permet de récupérer l'impacte factor d'un journal grâce à ce site -> https://www.resurchify.com/find/
    Args :
        articleDetail : L'article à analyser

    Returns : impactFactor (float) : l'impact factor du journal, null sinon

    """
    try:
        nameJournal = articleDetail.find('button', class_='journal-actions-trigger trigger')['title'].strip()
        impactFactor = getIFJournal(nameJournal)
    except AttributeError:
        impactFactor = 'null'
    return impactFactor


def getIFJournal(nameJournal: str):
    try:
        pageIF = requests.get(f'https://www.resurchify.com/find/?query={nameJournal}#search_results')
        soup = BeautifulSoup(pageIF.content, 'html.parser')

        spanList = soup.find_all('span', class_='w3-tag w3-medium w3-sand w3-border w3-margin-bottom')
        if len(spanList) > 0:
            IF = spanList[0].find('b').text.strip()
            IF = IF[14:]
        else:
            IF = 'null'
    except AttributeError:
        IF = 'null'
    return IF
