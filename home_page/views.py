from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'home_page/index.html')

