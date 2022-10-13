from tempfile import TemporaryFile
from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from .forms import *
from .models import *

# Create your views here.
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.  </body></html>" % now
    return HttpResponse(html)


# def home(request):
#     # Load all the food, then in the home.html we do for loop to show all the food objects
#     return render(request, "home.html", context)
    
def addFood(request):
    import json
    import requests
    form = foodForm()
    if request.method == 'POST':
        form = foodForm(request.POST)
        query = request.POST['quantity'] + request.POST['unit'] + " "+ request.POST['name']
        api_url = "https://api.calorieninjas.com/v1/nutrition?query="
        response = requests.get (api_url + query, headers ={'X-Api-Key': 'SeoEFgGuKRfRhHPo1+abzQ==xxVveS7IslW8qTa3'})
        temp = json.loads(response.content)['items']
        print(response.status_code)
        if response.status_code == requests.codes.ok and len(temp) != 0:

            temp = temp[0]
            food = attrForm()
            print(temp)
            food.sugar_g = temp['sugar_g']
            food.fiber_g = temp['fiber_g']
            food.serving_size_g = temp['serving_size_g']
            food.sodium_mg = temp['sodium_mg']
            food.name = temp['name']
            food.potassium_mg = temp['potassium_mg']
            food.fat_saturated_g = temp['fat_saturated_g']
            food.fat_total_g = temp['fat_total_g']
            food.calories = temp['calories']
            food.cholesterol_mg = temp['cholesterol_mg']
            food.protein_g = temp['protein_g']
            food.carbohydrates_total_g = temp['carbohydrates_total_g']
            #food.save()
            #print("Saved!")
            #return redirect('/')
        else: 
            return render(request, 'home.html', {'error': '!!!!!!!!!!!!!!'})
    context = {'form': form}
    return render(request, 'home.html', context)
