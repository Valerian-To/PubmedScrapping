"""
Module gérant la récupération du doi de l'article
"""


def getPmid(article):
    """
    Permet de récupérer le PMID de l'article à analyser
    Args :
        article : L'article à analyser

    Returns : pmid (str) : Le pmid de l'article

    """
    try:
        pmid = article.find("span", class_="citation-part").text.strip()
        pmid = pmid[6:]
    except AttributeError:
        pmid = "null"
    return pmid
