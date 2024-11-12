from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def home(request):
    return render(request, 'home.html')

def get_shop(request):
    return render(request, 'shop.html')

def get_basket(request):
    return render(request, 'basket.html')