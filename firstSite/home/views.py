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
from config import *

def home(request):
    goals = Goal.objects.all()
    now = datetime.now()
    todayMeals = Food.objects.all().filter(day__date = now)

    date = now.strftime("%B %d, %Y")

    calorieTotal = 0.00
    proteinTotal = 0.00

    for food in todayMeals:
        calorieTotal += food.calories
        proteinTotal += food.protein_g
    
    for goal in goals:
        if goal.nutrient == "protein":
            goal.progress = round((proteinTotal/float(goal.amount))*100,2)
        elif goal.nutrient == "calories":
            goal.progress = round((calorieTotal/float(goal.amount))*100,2)
        if goal.progress > 100: 
            goal.progress = 100.00

    context = {'today': todayMeals,'goals': goals, 'date': date}
    return render(request, "index.html", context)

def addFood(request):
    import json
    import requests
    form = foodForm()
    if request.method == 'POST':
        form = foodForm(request.POST)
        query = request.POST['quantity'] + request.POST['unit'] + " "+ request.POST['name']
        api_url = "https://api.calorieninjas.com/v1/nutrition?query="
        response = requests.get (api_url + query, headers ={'X-Api-Key': api_key})
        temp = json.loads(response.content)['items']
        if response.status_code == requests.codes.ok and len(temp) != 0:
            temp = temp[0]
            now = datetime.now()          
            food = Food(day=now, sugar_g=temp['sugar_g'], fiber_g=temp['fiber_g'], serving_size_g=temp['serving_size_g'] , 
                        sodium_mg=temp['sodium_mg'], name=temp['name'], potassium_mg=temp['potassium_mg'], fat_saturated_g=temp['fat_saturated_g'],
                        fat_total_g=temp['fat_total_g'], calories=temp['calories'], cholesterol_mg=temp['cholesterol_mg'], protein_g=temp['protein_g'],
                        carbohydrates_total_g=temp['carbohydrates_total_g'])
            food.save()
            return redirect('/')
        else: 
            return render(request, 'addFood.html', {'error': '!!!!!!!!!!!!!!'})
    context = {'form': form}
    return render(request, 'add.html', context)

def deleteFood(request, pk):
    import json
    import requests
    food = Food.objects.get(id=pk)
    if request.method == "POST":
        food.delete()
        return redirect('/')

    context = {'item':food}
    return render(request, 'delete.html', context)

def addGoal(request):
    goal = goalForm()
    if request.method == 'POST':
        goal = goalForm(request.POST)
        if goal.is_valid():
            goal.save()
            return redirect('/')
    context = {'goal':goal}
    return render(request, 'add-goal.html', context)

def deleteGoal(request, pk):
    goal = Goal.objects.get(id=pk)
    if request.method == "POST":
        goal.delete()
        return redirect('/')
    context = {'item':goal}
    return render(request, 'delete-Goal.html', context)