from bs4 import BeautifulSoup
import requests

from .listArticle import (
    getTitre,
    getAuteur,
    getPmid,
    getResume,
    isArticleFree,
    getArticleType
)

from .article import (
    getDoi,
    getCitation,
    getNbRefTotale,
    getKeyWords
)
from .impactFactor import (
    getIF
)

from .Journal import (
    getNameJournal
)


def getInfo(article):
    """
    Méthode qui récupère les informations dans l'article placé en paramètre

    Args :
        article : l'article a analysé

    Returns : une liste comprenant les informations récupérer de l'article

    """

    # Le titre de l'article
    titre = getTitre(article)

    # Le ou les auteur(s)
    auteur = getAuteur(article)

    # Le PMID de l'article
    pmid = getPmid(article)

    # Le résumé de l'article
    resume = getResume(article)

    # Indique si l'article est gratuit ou non
    free = isArticleFree(article)

    # Le type de l'article
    articleType = getArticleType(article)

    # On s'occupe du détail de chaque article
    r = requests.get(f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/")
    articleDetail = BeautifulSoup(r.content, "html.parser")

    # On récupère le doi
    doi = getDoi(articleDetail)

    # On récupère la citation de l'article
    citation = getCitation(articleDetail)

    # Le nombre de reference de l'article
    nbRef = getNbRefTotale(articleDetail)

    # La liste des mots clés de l'article
    keyWords = getKeyWords(articleDetail)

    # Le nom du journal
    journalName = getNameJournal(articleDetail)

    # L'ImpactFactor
    impactFactor = getIF(articleDetail)

    return [titre, auteur, resume, keyWords, citation, nbRef, pmid, doi, articleType, free, journalName, impactFactor]
