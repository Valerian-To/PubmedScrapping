"""
Module permettant de récupérer le nom du journal
"""


def getNameJournal(articleDetail):
    """
    Permet de récupérer le nom du journal qui a publié l'article
    Args :
        articleDetail : L'article a analysé

    Returns : nameJournal (str) : Le nom du journal, null sinon
    """
    try:
        nameJournal = articleDetail.find('button', class_='journal-actions-trigger trigger')['title'].strip()
    except AttributeError:
        nameJournal = 'null'
    return nameJournal
