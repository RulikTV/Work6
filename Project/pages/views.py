from django.shortcuts import render

def index1(request):
    return render(request, "home.html")

def index2(request):
    return render(request, "about.html")