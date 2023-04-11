"""
Module permettant la récupération du nombre de références totale
"""
import re


def getNbRefTotale(articleDetail):
    """
    Permet de récupérer le nombre total de références d'un article
    Args :
        articleDetail : L'article a analysé

    Returns : nbRef (int): le nombre de reference de l'article
    """
    try:
        # tableau contenant le bouton plus la liste des 5 premieres ref
        contenues = articleDetail.find('div', class_='refs-list')
        ref = contenues.find_all('li', class_='skip-numbering')

        try:
            # On extrait le texte du bouton pour récupérer le nombre de references qui ne sont pas affichées
            txtButton = articleDetail.find('button', class_='show-all').text
        except AttributeError:
            txtButton = ""

        # On appelle la méthode pour obtenir le nombre de références total
        nbRef = len(ref) + getNbRef(txtButton)
    except AttributeError:
        nbRef = 0
    return nbRef


def getNbRef(text: str):
    """
    Méthode qui permet d'extraire le nombre de références de la chaine de caractère

    Args :
        text (str) : la chaine avec le nombre de reference

    Returns :
        int : Le nombre de reference
    """
    if text == "":
        nbRef = 0
    else:
        chaine = re.findall(r'\d', text)
        nbRef = int(''.join(chaine))
    return nbRef
