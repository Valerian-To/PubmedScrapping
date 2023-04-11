from bs4 import BeautifulSoup
import requests
from bdd.connexionBDD import connexion
from data import getInfo
from bdd.Model import Article
from tqdm import tqdm


def scrapping():
    """
    Méthode qui permet de faire du scrapping
    sur le site de pubmed et d'enregistrer
    des infos dans un fichier CSV
    """

    listArticles = []

    for i in range(0, 3):
        # On enregistre le code HTML complet de la page pour récupérer la div contenant les articles
        url = f"https://pubmed.ncbi.nlm.nih.gov/?term=lung+cancer&sort=date&page={i+1}"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        div = soup.find('div', class_='search-results-chunk results-chunk')

        # Récupère les div pour chaque article et les insèrent dans une liste
        articles = div.find_all("article", class_="full-docsum")
        print(f"je scrape la page {i+1}")

        for unArticle in tqdm(articles, desc='article scrapper', unit='article', maxinterval=100):
            article = getInfo(unArticle)
            listArticles.append(article)
    connexion(listArticles)
