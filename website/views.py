from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib import messages

# Create your views here.
def index_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def menu_view(request):
    return render(request, 'menu.html')