from .parameter import Session, engine
from .Model.Article import Article
from .Model.Journal import Journal


def enregistrement(listArticle):
    """
    Permet d'enregistrer les informations en base de donnée
    """
    local_session = Session(bind=engine)
    listJournalORM = local_session.query(Journal).all()
    listArticleORM = local_session.query(Article).all()
    for article in listArticle:
        # unArticle = Article(
        #     titre=article[0],
        #     auteur=article[1],
        #     resume=article[2],
        #     motsCles=article[3],
        #     citation=article[4],
        #     nbRef=article[5],
        #     pmid=article[6],
        #     doi=article[7],
        #     type=article[8],
        #     isFree=article[9])
        # journalIsPresent(article, listJournalORM, unArticle)
        articleIsPresent(article, listArticleORM, listJournalORM)
    local_session.add_all(listArticleORM)
    local_session.add_all(listJournalORM)
    local_session.commit()


def journalIsPresent(article, listJournalORM, unArticle):
    """
    Permet de tester si un journal est déjà présent en base de donnée
    Args :
            article : L'article qui contient les données
            listJournalORM ([Journal]): La liste des journaux récupérés dans la base de donnée
            unArticle : L'article qui sera enregistrer
    """
    isPresent = False
    for i in listJournalORM:
        if i.nom == article[10]:
            isPresent = True
            unJournal = i

    if not isPresent:
        unJournal = Journal(nom=article[10], IF=article[11])
        listJournalORM.append(unJournal)
        unArticle.journals.append(unJournal)
    else:
        unArticle.journals.append(unJournal)
        isPresent = False


def articleIsPresent(article, listArticleORM, listJournalORM):
    """
    Permet de tester la présence d'un article dans la base de donnée
    Args :
            article : L'article qui contient les données
            listArticleORM ([Article]): La liste des articles récupérés dans la base de donnée
            listJournalORM ([Journal]): La liste des journaux récupérés dans la base de donnée
    """
    isPresent = False
    for i in listArticleORM:
        if i.titre == article[0]:
            isPresent = True
            unArticle = i
            break

    if not isPresent:
        unArticle = Article(
            titre=article[0],
            auteur=article[1],
            resume=article[2],
            motsCles=article[3],
            citation=article[4],
            nbRef=article[5],
            pmid=article[6],
            doi=article[7],
            type=article[8],
            isFree=article[9])
        listArticleORM.append(unArticle)
        journalIsPresent(article, listJournalORM, unArticle)
