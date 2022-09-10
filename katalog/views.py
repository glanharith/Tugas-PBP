from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):
    data_katalog = CatalogItem.objects.all()
    context = {
    'list_item': data_katalog,
    'nama': 'Glan Harith Teguh',
    'npm' : '2106752344'
    }
    return render(request, "katalog.html",context)
# TODO: Create your views here.
