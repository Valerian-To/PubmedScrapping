"""
Module qui permet de récupérer la liste des auteurs de l'article
"""


def getAuteurs(article):
    """
    Permet de récupérer la liste des auteurs de l'article

    Args :
        article : L'article à analyser

    Returns : auteurs (str[]) : La liste des auteurs de l'article
    """
    try:
        auteurs = article.find("span", class_="docsum-authors full-authors").text.strip()
    except AttributeError:
        auteurs = "null"
    return auteurs
