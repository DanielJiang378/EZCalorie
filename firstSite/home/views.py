from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.  </body></html>" % now
    return HttpResponse(html)

from .forms import InputForm
def home(request):
    context = {}
    form = InputForm(request.POST or None, request.FILES or None)
    context['form']=form
    return render(request, "home.html", context)