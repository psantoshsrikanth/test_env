from django.shortcuts import render
from django.http import HttpResponse
import datetime
import time
import inspect

def home(request):

    return render(request, 'home/Base.html', {'Home': 'home'})