from django.shortcuts import render, redirect
import requests


def index(request):
    url = 'https://data.nasa.gov/resource/gh4g-9sfh.json'
    r = requests.get(url).json()
    context = {'meteorites_data' : r}

    return render(request, "meteorite_app/index.html", context)

def search(request):
    name = request.POST['name']
    name = name.lower()
    name = name.title()
    print(name)

    if name == '':
        url = 'https://data.nasa.gov/resource/gh4g-9sfh.json'
        r = requests.get(url).json()
        context = {'meteorites_data' : r}
        return render(request, "meteorite_app/index.html", context)
    
    url = 'https://data.nasa.gov/resource/gh4g-9sfh.json?$where=lower(name)%20like%20lower(%22%25Aa%25%22)'
    r = requests.get(url).json()
    context = {'meteorites_data' : r}

    return render(request, "meteorite_app/search.html", context)