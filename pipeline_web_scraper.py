from global_config import config
import requests
from mongo.mongo_settings import collection_news
from bs4 import BeautifulSoup
from datetime import datetime



def scrape_full_content(url):
    # Faz a requisição HTTP para a URL
    response = requests.get(url)
    
    # Verifica se a requisição foi bem-sucedida
    if response.status_code != 200:
        return f"Failed to retrieve the page. Status code: {response.status_code}"
    
    # Analisa o HTML da página com BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Remover tags que normalmente contêm elementos indesejados (rodapés, comentários, anúncios)
    for element in soup(['script', 'style', 'aside', 'footer', 'nav','span']):
        element.extract()
    
    # Buscar o conteúdo do artigo a partir de <article> ou <div> com classes típicas
    article_tag = soup.find('article') or soup.find('div', class_='article-content')
    
    # Se o conteúdo for encontrado, extrair apenas os parágrafos
    if article_tag:
        paragraphs = article_tag.find_all('p')
        article_content = '\n'.join([p.get_text(strip=True) for p in paragraphs if len(p.get_text(strip=True)) > 50])
        return article_content

    # Caso nenhuma tag específica seja encontrada, tentar coletar todos os parágrafos da página
    paragraphs = soup.find_all('p')
    article_content = '\n'.join([p.get_text(strip=True) for p in paragraphs if len(p.get_text(strip=True)) > 50])
    
    return article_content or []


# Get URLS
project_format = {
    "$project": {
        "slug": 1,
        "url":1
    }
}

limit_stage = {
    "$limit":20
}

documents = list(collection_news.aggregate([project_format,limit_stage]))

# 'https://removed.com'


for document in documents:
    
    full_content_str = scrape_full_content(document["url"])
    
    if full_content_str:
        
        full_content_list = full_content_str.split("\n")

        filter_doc = {"slug":document["slug"]}
        update_doc = {
            "$set":{
                "web_scrape":{
                    "content":full_content_list,
                    "updated_at": datetime.utcnow()
                }
            }
        }
        
        collection_news.update_one(filter_doc,update_doc)
        
        print(f"Scraped page: {document['url']}")
