from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from time import sleep

@login_required
def home(request):
    return render(request, 'home/home.html')


def get_data(request):
    sleep(1)
    #fetch something from the database
    car = "Porche 911"

    return HttpResponse(car)