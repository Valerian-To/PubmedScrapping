"""
Module gérant la récupération du type de l'article
"""


def getArticleType(article):
    """
    Permet de récupérer le type de l'article

    Args :
        article : l'article à analyser

    Returns : type (str) : Le type de l'article
    """
    try:
        typeArticle = article.find('span', class_='publication-type spaced-citation-item citation-part').text.strip()
        typeArticle = typeArticle[:-1]
    except AttributeError:
        typeArticle = 'Article'
    return typeArticle
