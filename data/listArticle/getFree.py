"""
Module gérant la récupération de la mention de gratuité de l'article
"""


def isArticleFree(article):
    """
    Permet de savoir si l'article est gratuit ou non

    Args :
        article : l'article à analyser

    Returns : free (str) : retourne la chaine 'oui' si l'article est gratuit, sinon retourne 'non'
    """
    try:
        free = article.find("span", class_="free-resources spaced-citation-item citation-part").text.strip()
        free = "Oui"
    except AttributeError:
        free = "Non"
    return free
