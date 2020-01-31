from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'from_backend' : "I am from Backend"}
    return render(request, 'first_app/index.html', context=my_dict)

def index1(request):
    return HttpResponse("<h1 style="+"text-align:center;"+">Home Page of MY Dj Animated Happiness</h1>")