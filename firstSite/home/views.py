from tempfile import TemporaryFile
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .forms import InputForm

# Create your views here.
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.  </body></html>" % now
    return HttpResponse(html)


def home(request):
    context = {}
    form = InputForm(request.POST or None, request.FILES or None)
    context['form']=form
    print(request.POST)
    return render(request, "home.html", context)
    
def createFood(request):
    import json
    import requests
    name = request.POST['name']
    quantity = request.POST['quantity']
    unit = request.POST['unit']
    query = unit + quantity + name
    api_url = "https://api.calorieninjas.com/v1/nutrition?query="
    response = requests.get (api_url + query, headers ={'X-Api-Key': 'SeoEFgGuKRfRhHPo1+abzQ==xxVveS7IslW8qTa3'})
    try:
        res=json.loads(response.content)
        print(response.content)
    except Exception as e:
        res = "oops there was an error"
        print(e)
    return render(request, 'home.html',{'res': res})