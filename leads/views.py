from django.shortcuts import render
from django.http import HttpResponse

# Create  views.


def home_page(request):
    return HttpResponse("Hello World")
