from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus
BASE_CRAIGLIST_URL = 'https://sfbay.craigslist.org/search/?query={}'
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'
from . import models

# Create your views here.
def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    print(search)
    models.Search.objects.create(search=search)
    final_url = BASE_CRAIGLIST_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    post_listings = soup.find_all('li', {'class': 'result-row'})
    # print(post_listings[0])
    # post_titles = post_listings[0].find(class_='result-title').text
    # post_url = post_listings[0].find('a').get('href')
    # post_price = post_listings[0].find(class_='result-price').text
    final_postings = []
    for post in post_listings:
        post_titles = post.find(class_='result-title').text
        post_url = post.find('a').get('href')
        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price = "N/A"
        if post.find(class_="result-image").get('data-ids'):
            post_image = post.find(class_="result-image").get('data-ids').split(",")[0].split(":")[1]
            post_image_url = BASE_IMAGE_URL.format(post_image)
        else:
            post_image_url = 'https://craigslist.org/images/peace.jpg'
            # print(post_image_url)
        final_postings.append((post_titles, post_url, post_price, post_image_url))

    stuff_for_frontend = {
        'search': search,
        'final_postings': final_postings,
                          }
    return render(request, 'myapp/new_search.html', stuff_for_frontend)

def used_cars(request):
    search = "used cars"
    final_url = BASE_CRAIGLIST_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    post_listings = soup.find_all('li', {'class': 'result-row'})
    # print(post_listings[0])
    # post_titles = post_listings[0].find(class_='result-title').text
    # post_url = post_listings[0].find('a').get('href')
    # post_price = post_listings[0].find(class_='result-price').text
    final_postings = []
    for post in post_listings:
        post_titles = post.find(class_='result-title').text
        post_url = post.find('a').get('href')
        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price = "N/A"
        if post.find(class_="result-image").get('data-ids'):
            post_image = post.find(class_="result-image").get('data-ids').split(",")[0].split(":")[1]
            post_image_url = BASE_IMAGE_URL.format(post_image)
        else:
            post_image_url = 'https://craigslist.org/images/peace.jpg'
            # print(post_image_url)
        final_postings.append((post_titles, post_url, post_price, post_image_url))
        stuff_for_frontend = {
            'search': search,
            'final_postings': final_postings,
        }
    return render(request, 'myapp/used_cars.html', stuff_for_frontend)

def electronics(request):
    search = "electronics"
    final_url = BASE_CRAIGLIST_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    post_listings = soup.find_all('li', {'class': 'result-row'})
    # print(post_listings[0])
    # post_titles = post_listings[0].find(class_='result-title').text
    # post_url = post_listings[0].find('a').get('href')
    # post_price = post_listings[0].find(class_='result-price').text
    final_postings = []
    for post in post_listings:
        post_titles = post.find(class_='result-title').text
        post_url = post.find('a').get('href')
        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price = "N/A"
        if post.find(class_="result-image").get('data-ids'):
            post_image = post.find(class_="result-image").get('data-ids').split(",")[0].split(":")[1]
            post_image_url = BASE_IMAGE_URL.format(post_image)
        else:
            post_image_url = 'https://craigslist.org/images/peace.jpg'
            # print(post_image_url)
        final_postings.append((post_titles, post_url, post_price, post_image_url))
        stuff_for_frontend = {
            'search': search,
            'final_postings': final_postings,
        }
    return render(request, 'myapp/electronics.html', stuff_for_frontend)

def fashion(request):
    search = "fashion"
    final_url = BASE_CRAIGLIST_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    post_listings = soup.find_all('li', {'class': 'result-row'})
    # print(post_listings[0])
    # post_titles = post_listings[0].find(class_='result-title').text
    # post_url = post_listings[0].find('a').get('href')
    # post_price = post_listings[0].find(class_='result-price').text
    final_postings = []
    for post in post_listings:
        post_titles = post.find(class_='result-title').text
        post_url = post.find('a').get('href')
        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price = "N/A"
        if post.find(class_="result-image").get('data-ids'):
            post_image = post.find(class_="result-image").get('data-ids').split(",")[0].split(":")[1]
            post_image_url = BASE_IMAGE_URL.format(post_image)
        else:
            post_image_url = 'https://craigslist.org/images/peace.jpg'
            # print(post_image_url)
        final_postings.append((post_titles, post_url, post_price, post_image_url))
        stuff_for_frontend = {
            'search': search,
            'final_postings': final_postings,
        }
    return render(request, 'myapp/fashion.html', stuff_for_frontend)

def jobs(request):
    search = "jobs"
    final_url = BASE_CRAIGLIST_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    post_listings = soup.find_all('li', {'class': 'result-row'})
    # print(post_listings[0])
    # post_titles = post_listings[0].find(class_='result-title').text
    # post_url = post_listings[0].find('a').get('href')
    # post_price = post_listings[0].find(class_='result-price').text
    final_postings = []
    for post in post_listings:
        post_titles = post.find(class_='result-title').text
        post_url = post.find('a').get('href')
        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price = "N/A"
        if post.find(class_="result-image").get('data-ids'):
            post_image = post.find(class_="result-image").get('data-ids').split(",")[0].split(":")[1]
            post_image_url = BASE_IMAGE_URL.format(post_image)
        else:
            post_image_url = 'https://craigslist.org/images/peace.jpg'
            # print(post_image_url)
        final_postings.append((post_titles, post_url, post_price, post_image_url))
        stuff_for_frontend = {
            'search': search,
            'final_postings': final_postings,
        }
    return render(request, 'myapp/jobs.html', stuff_for_frontend)

def toys(request):
    search = "toys"
    final_url = BASE_CRAIGLIST_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    post_listings = soup.find_all('li', {'class': 'result-row'})
    # print(post_listings[0])
    # post_titles = post_listings[0].find(class_='result-title').text
    # post_url = post_listings[0].find('a').get('href')
    # post_price = post_listings[0].find(class_='result-price').text
    final_postings = []
    for post in post_listings:
        post_titles = post.find(class_='result-title').text
        post_url = post.find('a').get('href')
        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price = "N/A"
        if post.find(class_="result-image").get('data-ids'):
            post_image = post.find(class_="result-image").get('data-ids').split(",")[0].split(":")[1]
            post_image_url = BASE_IMAGE_URL.format(post_image)
        else:
            post_image_url = 'https://craigslist.org/images/peace.jpg'
            # print(post_image_url)
        final_postings.append((post_titles, post_url, post_price, post_image_url))
        stuff_for_frontend = {
            'search': search,
            'final_postings': final_postings,
        }
    return render(request, 'myapp/toys.html', stuff_for_frontend)

def housing(request):
    search = "housing"
    final_url = BASE_CRAIGLIST_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    post_listings = soup.find_all('li', {'class': 'result-row'})
    # print(post_listings[0])
    # post_titles = post_listings[0].find(class_='result-title').text
    # post_url = post_listings[0].find('a').get('href')
    # post_price = post_listings[0].find(class_='result-price').text
    final_postings = []
    for post in post_listings:
        post_titles = post.find(class_='result-title').text
        post_url = post.find('a').get('href')
        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price = "N/A"
        if post.find(class_="result-image").get('data-ids'):
            post_image = post.find(class_="result-image").get('data-ids').split(",")[0].split(":")[1]
            post_image_url = BASE_IMAGE_URL.format(post_image)
        else:
            post_image_url = 'https://craigslist.org/images/peace.jpg'
            # print(post_image_url)
        final_postings.append((post_titles, post_url, post_price, post_image_url))
        stuff_for_frontend = {
            'search': search,
            'final_postings': final_postings,
        }
    return render(request, 'myapp/housing.html', stuff_for_frontend)