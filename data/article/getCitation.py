"""
Module gérant la récupération de la citation de l'article
"""


def getCitation(articleDetail):
    """
    Permet de récupérer la citation de l'article
    Args :
        articleDetail : L'article à analyser

    Returns : citation (str) : la citation de l'article, null sinon

    """
    try:
        nameJournal = articleDetail.find('button', class_='journal-actions-trigger trigger')['title']
        date = articleDetail.find('div', class_="cit").text.strip()
        doi = articleDetail.find('span', class_='citation-doi')
        citation = nameJournal + ' ' + date + ' ' + doi
    except AttributeError:
        citation = "null"
    return citation
