from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name="home"),
    path('news/<str:slug>/', views.news_view, name = "news-detail"),
]