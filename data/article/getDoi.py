"""
Module gérant la récupération du doi de l'article
"""


def getDoi(articleDetail):
    """
    Permet de récupérer le DOI de l'article
    Args :
        articleDetail : L'article a analysé

    Returns : doi (str) : Le DOI de l'article, null sinon
    """
    try:
        doi = articleDetail.find("a", class_="id-link").text.strip()
    except AttributeError:
        doi = "null"
    return doi
