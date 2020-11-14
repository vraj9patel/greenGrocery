from django.shortcuts import render
from products.models import Product

def index(request):
    qs = Product.objects.featured()
    dict = {
        # 'form': form
        'qs': qs,
        'btn': 'index',
        'lst': ['Dragon Fruit', 'Papaya', 'Pineapple', 'Sugarcane']
    }
    return render(request, "index.html", context=dict)

def about(request):
    return render(request, "about.html", {'btn':'about'})