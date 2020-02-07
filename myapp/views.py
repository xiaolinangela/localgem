from django.shortcuts import render
from bs4 import BeautifulSoup
import request

# Create your views here.
def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    stuff_for_frontend = {'search': search, }
    return render(request, 'myapp/new_search.html', stuff_for_frontend)