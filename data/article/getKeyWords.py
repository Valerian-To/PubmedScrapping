"""
Module gérant la récupération de la liste de mots clés d'un article
"""


def getKeyWords(articleDetail):
    """
    Permet de récupérer la liste des mots clés d'un article
    Args :
        articleDetail : L'article a analysé

    Returns : keyWords (str) : La liste de mots clés, null sinon
    """
    try:
        # tableau contenant le bouton plus la liste des 5 premieres ref
        contenues = articleDetail.find('div', class_='abstract')
        listP = contenues.find_all('p')
        listWords = getKeyWords(listP)
        keyWord = ''
        for word in listWords:
            keyWord += word
    except AttributeError:
        keyWord = 'null'
    return keyWord
