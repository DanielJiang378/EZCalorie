from tempfile import TemporaryFile
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .forms import foodForm
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
        query = request.POST['quantity'] + request.POST['unit'] + " " + request.POST['name']
        api_url = "https://api.calorieninjas.com/v1/nutrition?query="
        response = requests.get (api_url + query, headers ={'X-Api-Key': 'SeoEFgGuKRfRhHPo1+abzQ==xxVveS7IslW8qTa3'})
        print(json.loads(response.content))
        print(response.content)
        # if food.is_valid():
        #     food.save()
        #     return redirect('/')

    context = {'form': form}
    return render(request, 'home.html', context)