from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

tax_rate = 0.15

def index(request):
    return render(request,"newapp/index.html")


def calculate(request, number):
    total_price = number + (number * tax_rate)
    return HttpResponse(f"The total price after tax is: {total_price}")


def taxrate(request):
    return render(request, "newapp/taxrate.html", {"tax_rate": tax_rate})