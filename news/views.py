from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from mongo.mongo_settings import collection_news
from news.utils import increment_news
from datetime import datetime

def home_view(request):
    
    # Filter List News
    start_date = datetime(2024, 1, 1)  # 1º de Janeiro de 2024
    end_date = datetime(2024, 12, 30, 23, 59, 59)  # 30 de Dezembro de 2024, final do dia
    
    filter_parameters = { 
        # images not empty (I could skip this and put in the pipeline to avoid populate the DB with rubish information)
        "image_url":{"$ne":None},
        # Filter List News
        "date_published": {
            "$gte": start_date,  # Data maior ou igual a 1º de janeiro de 2024
            "$lte": end_date     # Data menor ou igual a 29 de fevereiro de 2024
        },
        # Filter Content
        # "content":{"$ne":None},
        "web_scrape":{"$exists":True}   
    }
    
    # Get first n News
    n = 100
    news_list = list(
        collection_news.find(filter_parameters).limit(n)
        )
    
    return render(request, 'home.html', {"news_list":news_list})

def news_view(request, slug):
    
    news = collection_news.find_one({"slug":slug})
    if news:
        
        # Increment view field by visiting
        increment_news(slug=slug)
    
        return render(request,'news.html',{"news":news})
    return HttpResponse("<h1>Not found in our DB</h1>")
