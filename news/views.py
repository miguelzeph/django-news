from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from mongo.mongo_settings import collection_news
from news.utils import increment_news

def home_view(request):
    
    # Get List News
    news_list = list(collection_news.find({}))
    return render(request, 'home.html', {"news_list":news_list})

def news_view(request, slug):
    
    news = collection_news.find_one({"slug":slug})
    if news:
        
        increment_news(slug=slug)
    
        return render(request,'news.html',{"news":news})
    return HttpResponse("<h1>Not found in our DB</h1>")
