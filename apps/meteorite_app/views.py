from django.shortcuts import render, redirect
import requests


def index(request):
    url = 'https://data.nasa.gov/resource/gh4g-9sfh.json'
    r = requests.get(url).json()

    context = {'meteorites_data' : r}

    return render(request, "meteorite_app/index.html", context)

def search(request):
    name = request.POST['name']
    url = 'https://data.nasa.gov/resource/gh4g-9sfh.json?name={}'.format(name)
    r = requests.get(url).json()

    context = {'meteorites_data' : r}

    return render(request, "meteorite_app/search.html", context)