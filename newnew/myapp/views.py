from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


tax_rate = 0.15

def index(request):
    return render(request,"myapp/index.html")



def num(request, number):
    total_price = number + (number * tax_rate)
   # return HttpResponse(f"The total price after tax is: {total_price}")


def taxrate(request):
    return render(request, "myapp/taxrate.html", {"tax_rate": tax_rate})