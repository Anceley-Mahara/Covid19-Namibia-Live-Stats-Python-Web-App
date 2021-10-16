from django.shortcuts import render
from urllib.request import urlopen
import requests
import json

# Create your views here.
def home(request):
    url = "https://covid-193.p.rapidapi.com/statistics"

    queryString = {"country": "Namibia"}

    headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "958fd62232mshcc85ab936e95237p158994jsn835fe2a4bfac"
    }

    response = requests.request("GET", url, headers=headers, params=queryString).json()

    data = response['response']

    d = data[0]

    print(d)

    results ={
         'all': d['cases']['total'],
         'recovered': d['cases']['recovered'],
         'deaths': d['deaths']['total'],
         'new': d['cases']['new'],
         'critical': d['cases']['critical'],

     }

   
    return render(request,'index.html', results)
