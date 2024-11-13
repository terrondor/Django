from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home.html')


def get_shop(request):
    games = {'games': ["Escape from Tarkov", "Grand Thief Auto V", "IRacing"], }
    return render(request, 'shop.html', games)



def get_basket(request):
    return render(request, 'basket.html')
