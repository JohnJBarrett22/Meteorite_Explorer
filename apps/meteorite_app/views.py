from django.shortcuts import render, redirect
import requests

# Create your views here.
def index(request):
    url = 'https://data.nasa.gov/resource/gh4g-9sfh.json'
    r = requests.get(url)
    print(r.text.encode("utf-8"))

    return render(request, "meteorite_app/index.html")