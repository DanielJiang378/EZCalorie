from tempfile import TemporaryFile
from time import strftime
from turtle import st
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime
from django.urls import is_valid_path
from .forms import *
from .models import *
from datetime import datetime

# Create your views here.
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.  </body></html>" % now
    return HttpResponse(html)


def home(request):
    goals = Goal.objects.all()    
    #foods = Food.objects.all()
    now = datetime.now()
    #time = now.strftime("%m") + "/" + now.strftime("%d") + "/" + now.strftime("%Y")
    #todayMeals = [obj for obj in Food.objects.all() if obj.day == now]
    todayMeals = Food.objects.all().filter(day__date = now)
    #foods = Food.objects.all().filter(day__date = now)

    date = now.strftime("%B %d, %Y")
    time = now.strftime("%H:%M:%S")

    calorieTotal = 0.00
    proteinTotal = 0.00

    calorieTotal = 0.00
    proteinTotal = 0.00

    for food in todayMeals:
        calorieTotal += food.calories
    for food in todayMeals:
        proteinTotal = food.protein_g
    
    for goal in goals:
        if goal.nutrient == "protein":
            print(goal.progress)
            goal.progress = round((proteinTotal/float(goal.amount))*100,3)
        elif goal.nutrient == "calories":
            print(goal.progress)
            goal.progress = round((calorieTotal/float(goal.amount))*100,3)
        if goal.progress > 100: 
            goal.progress = 100.00

    context = {'today': todayMeals,'goals': goals}
    return render(request, "index.html", context)

# def day(request): 
#     day = Day.objects.get(id=pk_test)
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

            now = datetime.now()
            food = Food(day=now, sugar_g=temp['sugar_g'], fiber_g=temp['fiber_g'], serving_size_g=temp['serving_size_g'] , 
                        sodium_mg=temp['sodium_mg'], name=temp['name'], potassium_mg=temp['potassium_mg'], fat_saturated_g=temp['fat_saturated_g'],
                        fat_total_g=temp['fat_total_g'], calories=temp['calories'], cholesterol_mg=temp['cholesterol_mg'], protein_g=temp['protein_g'],
                        carbohydrates_total_g=temp['carbohydrates_total_g'])
  
            #print(temp)
            food.save()
            print('saved')
            return redirect('/')
        else: 
            return render(request, 'addFood.html', {'error': '!!!!!!!!!!!!!!'})
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

def addGoal(request):
    import json
    import requests
    goal = goalForm()
    if request.method == 'POST':
        goal = goalForm(request.POST)
        if goal.is_valid():
            goal.save()
            return redirect('/')
    context = {'goal':goal}
    return render(request, 'add-goal.html', context)

def deleteGoal(request, pk):
    import json
    import requests
    goal = Goal.objects.get(id=pk)
    print(goal)
    if request.method == "POST":
        goal.delete()
        print('delete')
        return redirect('/')
    context = {'item':goal}
    return render(request, 'delete-Goal.html', context)