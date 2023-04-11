"""
Module gérant la récupération du résumé de l'article
"""


def getResume(article):
    """
    Permet de récupérer le résumé de l'article à analyser

    Args :
        article : L'article à analyser

    Returns : resume (str) : Le résumé de l'article
    """
    try:
        resume = article.find("div", class_="full-view-snippet").text.strip()
        if resume == "":
            resume = "null"
    except AttributeError:
        resume = "null"
    return resume
