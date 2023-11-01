from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:number>/", views.calculate, name="calculate"),
    path("taxrate/", views.taxrate, name="taxrate")
]