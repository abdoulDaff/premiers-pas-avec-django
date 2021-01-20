from django.shortcuts import render
from django.http import HttpResponse

# Create  views.


def home_page(request):
    context = {}
    return render(request, "second_page.html", context)
