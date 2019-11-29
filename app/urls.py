from django.urls import path 
from app import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('home/', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('pricing/', views.Pricing.as_view(), name='pricing'),
    path('terms/', views.Terms.as_view(), name='terms'),
    path('book-our-adventures/', views.BookAdventure.as_view(), 
        name='book-our-adventures'),
    path('eat/', views.Eat.as_view(), name='eat'),
    path('play/', views.Play.as_view(), name='play'),
    path('relax/', views.Relax.as_view(), name='relax'),
    
]
