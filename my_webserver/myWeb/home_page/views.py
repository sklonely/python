from django.shortcuts import render
from django.http import HttpResponse
import sys


# Create your views here.
def index(request):
    # View code here...
    return render(request, 'home_page.html', {'title': "Sklonely's home", 'data': "This is home page"})
