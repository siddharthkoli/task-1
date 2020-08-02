from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def home(req):
    numbers = []
    for i in range(20):
        numbers.append(i + 1)
    return render(req, "task1/home.html", {
        'numbers': numbers
    })


def generateNumbers(req):
    if req.method == "POST":
        numbers = []
        startPoint = req.POST.get("startPoint")
        endPoint = req.POST.get("endPoint")
        if startPoint == '' or endPoint == '':
            messages.error(req, "Enter all fields.")
            return render(req, "task1/home.html")
        startPoint = int(startPoint)
        endPoint = int(endPoint)
        if endPoint < startPoint:
            messages.error(req, "Starting Point should be less than Ending Point.")
            return render(req, "task1/home.html")
        for i in range(startPoint, endPoint + 1):
            numbers.append(i)
        return render(req, "task1/home.html", {
            'numbers': numbers
        })
