from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from mongo.mongo_settings import collection_news

def home_view(request):
    
    news_list = list(collection_news.find({}))

    return render(request, 'home.html', {"news_list":news_list})

def news_view(request, slug):
    
    news = collection_news.find_one({"slug":slug})
    
    if news:
    
        return render(
            request,
            'news.html',
            news # Content
        )
    
    return HttpResponse("<h1>Not found in our DB</h1>")

