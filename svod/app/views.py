
import datetime
from django.contrib import messages
from django.http import Http404, HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import *

from django.utils import timezone

from datetime import date
# Create your views here.
def login(request: HttpRequest):

    if(request.COOKIES.get('otd')):
        return redirect('main')

    if (request.POST):
        id = request.POST['itotd']
        
        otd = Otd.objects.filter(idotd = id)
        
        if(len(otd) == 0):
            messages.add_message(request, messages.INFO, 'Нет такого отделения')
            return redirect('login')
        
        response = redirect('main')
        response.set_cookie('otd',otd[0].idotd, max_age=60 * 120)
        return response
    
    return render(request, 'app/login.html')
    

def main(request: HttpRequest):
    if(request.COOKIES.get('otd') == None):
        print(request.COOKIES.get('otd'))

    otd_id = request.COOKIES.get('otd')

    try:
        otd = Otd.objects.get(idotd = otd_id)
    except Otd.DoesNotExist:
        raise Http404('нет такого отделения')

    context = {
        'otd': otd
    }
    return render(request, 'app/main.html', context=context)



def logout(request: HttpRequest):
    response = redirect('login')
    response.delete_cookie('otd')
    return response




def get_otds(request: HttpRequest):
    if(request.COOKIES.get('otd') == None):
        redirect('login')
    
    otds = Otd.objects.all()

    if (len(otds) != 0):
        context = {
            'otds': otds
        }
        
        return render(request, 'app/Otd_lists.html', context)

    return render(request, 'app/Otd_lists.html')




def otd_details(request: HttpRequest, idotd : int):
    try:
        otd = get_object_or_404(Otd, pk=idotd)
    except Otd.DoesNotExist:
        raise Http404("No MyModel matches the given query.")
    return render(request, 'app/otd_details.html', context={'otd': otd})


def food_svod(request: HttpRequest):
    if(request.COOKIES.get('otd') == None):
        return redirect('login')
    
    otd_id = request.COOKIES.get('otd')

    otd = Otd.objects.get(idotd = otd_id)
    food_svod = otd.food_svod_set.all()

    print(len(food_svod))

    context = {
        'svod': food_svod,
        'otd': otd
    }
    return render(request, 'app/food_svod.html', context=context)


