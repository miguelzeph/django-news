from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from mongo.mongo_settings import collection_news
from datetime import datetime

class NewsSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        # Defina o intervalo de datas ou outros filtros que desejar
        start_date = datetime(2024, 1, 1)
        end_date = datetime(2024, 12, 30, 23, 59, 59)
        
        filter_parameters = {
            "image_url": {"$ne": None},
            "date_published": {
                "$gte": start_date,
                "$lte": end_date
            }
        }
        
        # Retorne a lista de notícias do MongoDB
        return list(collection_news.find(filter_parameters))
    
    def location(self, obj):
        # Gera a URL de cada notícia
        return reverse('news-detail', args=[obj['slug']])
    
    def lastmod(self, obj):
        # Retorne a data de modificação da notícia
        return obj['date_published']
