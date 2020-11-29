from django.shortcuts import render
from django.http import HttpResponse
import datetime
import time
import inspect
def time_home(request):
    now = mul_time_cal([Fibonacci(10),Fibonacci(20),Fibonacci(30)])
    html = "<html><body>Duration of functions is %s.</body></html>" % now
    return HttpResponse(html)

def Fibonacci(n):
    if n<=0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

def time_cal(fun):
    t1 = time.perf_counter()
    fun
    t2 = time.perf_counter()
    return t2-t1

def mul_time_cal(series):
    time_series = []
    for func in series:
        duration = time_cal(func)
        time_series.append(duration)
    return time_series