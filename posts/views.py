from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_page_view(request):
    return HttpResponse("Welcome to The Hot Hatch Club Homepage!")


def my_posts(request):
    return HttpResponse("Welcome to The Hot Hatch Club!")
