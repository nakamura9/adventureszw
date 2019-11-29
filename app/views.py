from django.shortcuts import render
from django.views.generic import TemplateView,DetailView
from app.models import Adventure
import os

class Home(TemplateView):
    template_name = os.path.join('app', 'home.html')

class About(TemplateView):
    template_name = os.path.join('app', 'about.html')

class Pricing(TemplateView):
    template_name = os.path.join('app', 'pricing.html')

class Eat(TemplateView):
    template_name = os.path.join('app', 'eat.html')

class Play(TemplateView):
    template_name = os.path.join('app', 'play.html')

class Relax(TemplateView):
    template_name = os.path.join('app', 'relax.html')

class BookAdventure(TemplateView):
    template_name = os.path.join('app', 'book_adventure.html')

class Events(TemplateView):
    template_name = os.path.join('app', 'home.html')

class Terms(TemplateView):
    template_name = os.path.join('app', 'terms.html')

class AdventureDetail(DetailView):
    model = Adventure
    template_name = os.path.join('app', 'details.html')
