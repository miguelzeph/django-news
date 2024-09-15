from django.db import models
from django.utils.text import slugify
from datetime import datetime
from mongo.mongo_settings import collection_news

class News:
    
    def __init__(
        self,
        title:str,
        content:str,
        image_url:str,
        date_published:datetime,
        author:str,
        tags:list,
        category:str,
        source:str
        ):
        
        self.title = title
        self.content = content
        self.image_url = image_url
        self.date_published = date_published
        self.author = author
        self.tags = tags
        self.category = category
        self.source = source
        
    def processing_news(self):
        
        self.news_document = {
            "title": self.title,
            "content": self.content,
            "slug": slugify(self.title),
            "image_url": self.image_url,
            "date_published": self.date_published,
            "author": self.author,
            "tags": self.tags,
            "category": self.category,
            "source": self.source
            # language (AI can define)
        }
            
    def save_to_db(self):
        
        # Process Data
        self.processing_news()
        
        # Save    
        collection_news.insert_one(self.news_document)
    
