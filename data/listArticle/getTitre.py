"""
Module qui permet de récupérer le titre de l'article et le mets en forme
"""


def getTitre(article):
    """
    Permet de récupérer le titre de l'article
    Args :
        article : L'article a analysé

    Returns :
        titre (str) : Le titre formater

    """
    try:
        titre = article.find("a").text.strip()
        titre = titreFormat(titre)
    except AttributeError:
        titre = "null"
    return titre


def titreFormat(titre: str):
    """
    Modifie le titre pour qu'il soit plus lisible lors de l'enregistrement

    Args :
        titre (str): le titre récupéré

    Returns :
        str : le titre
    """
    charDel = ["[", "]", "\'"]
    titre = titre.translate(str.maketrans('', '', ''.join(charDel)))
    return titre
