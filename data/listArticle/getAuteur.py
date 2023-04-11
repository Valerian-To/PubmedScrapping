"""
Module qui permet de récupérer la liste des auteurs de l'article
"""


def getAuteur(article):
    """
    Permet de récupérer la liste des auteurs de l'article

    Args :
        article : L'article à analyser

    Returns : auteur (str[]) : La liste des auteurs de l'article
    """
    try:
        auteur = article.find("span", class_="docsum-authors full-authors").text.strip()
    except AttributeError:
        auteur = "null"
    return auteur
