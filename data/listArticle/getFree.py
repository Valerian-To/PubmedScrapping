"""
Module gérant la récupération de la mention de gratuité de l'article
"""


def isArticleFree(article):
    """
    Permet de savoir si l'article est gratuit ou non

    Args :
        article : l'article à analyser

    Returns : free (boolean) : retourne True si l'article est gratuit, sinon False
    """
    try:
        free = article.find("span", class_="free-resources spaced-citation-item citation-part").text.strip()
        free = True
    except AttributeError:
        free = False
    return free
