from tempfile import TemporaryFile
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime
from django.urls import is_valid_path
from .forms import *
from .models import *

# Create your views here.
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.  </body></html>" % now
    return HttpResponse(html)


def home(request):
    foods = Food.objects.all()

    context = {'foods': foods}
    return render(request, "home.html", context)
    
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
        #print(response.status_code)
        if response.status_code == requests.codes.ok and len(temp) != 0:

            temp = temp[0]
            food = Food(sugar_g=temp['sugar_g'], fiber_g=temp['fiber_g'], serving_size_g=temp['serving_size_g'] , 
                        sodium_mg=temp['sodium_mg'], name=temp['name'], potassium_mg=temp['potassium_mg'], fat_saturated_g=temp['fat_saturated_g'],
                        fat_total_g=temp['fat_total_g'], calories=temp['calories'], cholesterol_mg=temp['cholesterol_mg'], protein_g=temp['protein_g'],
                        carbohydrates_total_g=temp['carbohydrates_total_g'])
            print(temp)
            food.save()
            print('saved')
            return redirect('/')
        else: 
            return render(request, 'add.html', {'error': '!!!!!!!!!!!!!!'})
    context = {'form': form}
    return render(request, 'add.html', context)

def deleteFood(request, pk):
    import json
    import requests
    food = Food.objects.get(id=pk)
    print(food)
    if request.method == "POST":
        food.delete()
        print('delete')
        return redirect('/')

    context = {'item':food}
    return render(request, 'delete.html', context)
