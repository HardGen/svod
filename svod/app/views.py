
from openpyxl import Workbook
import datetime
import json
from django.contrib import messages
from django.http import Http404, HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import *
from django.core import serializers

from django.utils import timezone

from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font

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

    context = {
        'svod': food_svod,
        'otd': otd
    }
    return render(request, 'app/food_svod.html', context=context)


def get_svod_by_date(request: HttpRequest, year: int, month: int, day:int):
    otd_id = request.COOKIES.get('otd')
    svod = Otd.objects.get(pk=otd_id)
    result = svod.food_svod_set.filter(
        dt_svood__year = year,
        dt_svood__month = month,
        dt_svood__day = day
    )

    if (result.count() == 0):
        return JsonResponse({
            'length': 0
    })

    data = serializers.serialize("json",result)
    return JsonResponse({
        'length': result.count(),
        'svod': data,
    })

def update_value(request: HttpRequest):
    column = request.POST['column']
    time = request.POST['time']
    time2 = "2023-03-21 08:57:02"
    value = request.POST['value']
    otd_id = request.COOKIES.get('otd')
    dt = datetime.datetime.strptime(time,  "%Y-%m-%d %H:%M:%S")
    svod = Food_svod.objects.get(idotd_id=otd_id, dt_svood__icontains=dt)
    if column == 'vsego':
        svod.vsego = value
    if column == 'child':
        svod.child = value
    if column == 'mam':
        svod.mam = value
    if column == 'mam_nofood':
        svod.mam_nofood = value
    if column == 'wow':
        svod.wow = value
    if column == 'zond':
        svod.zond = value
    if column == 'golod':
        svod.golod = value
    if column == 'diet_01_kis':
        svod.diet_01_kis = value
    if column == 'diet_01_bul':
        svod.diet_01_bul = value
    if column == 'diet_02':
        svod.diet_02 = value
    if column == 'diet_03':
        svod.diet_03 = value
    if column == 'diet_ovd':
        svod.diet_ovd = value
    if column == 'diet_shd':
        svod.diet_shd = value
    if column == 'diet_child':
        svod.diet_child = value
    if column == 'diet_vdb':
        svod.diet_vdb = value
    if column == 'diet_nbd':
        svod.diet_nbd = value
    if column == 'diet_nkd':
        svod.diet_nkd = value
    svod.save()

    return JsonResponse({'otd': serializers.serialize('json', [svod, ])})
    

def create_new_food_svod(request: HttpRequest):
    otd = Otd.objects.get(pk=request.COOKIES.get('otd'))
    new_food_svod = otd.food_svod_set.create()


    return JsonResponse({
        'svod': serializers.serialize('json', [new_food_svod, ])
    })



def report(request: HttpRequest, datetm:str ):
    otd_id = Otd.objects.get(pk=request.COOKIES.get('otd'))
    d = datetime.datetime.strptime(datetm, "%Y-%m-%d")

    svod = Food_svod.objects.get(idotd_id=otd_id, 
        dt_svood__year = d.date().year,
        dt_svood__month = d.date().month,  
        dt_svood__day = d.date().day,                   
    )
    
    create_report_seven(svod, d.date(), "СВОДКА ПИТАНИЯ")

    return JsonResponse({
        'message': 'success'
    })

def create_report_seven(svod: Food_svod, d: date, title:str):
    alignment = Alignment(
        horizontal='right'
    )
    font = Font(
        size= 6
    )
    try:
        wb = Workbook()
        ws = wb.active
        ws['N1'] = 'Форма №1-84'
        ws['N1'].alignment = alignment
        ws['N1'].font = font
        ws['N2'] = 'к Инструкции по организации лечебного питания'
        ws['N2'].alignment = alignment
        ws['N2'].font = font
        ws['N3'] = 'в лечебно-проф.учреждениях КГБУЗ "НМБ №1"'
        ws['N3'].alignment = alignment
        ws['N3'].font = font
        ws['A4'] = title

        

        ws['A8'] = "На 7:00"
        cell = ws['E8']
        cell.value = d
        cell.number_format = 'YYYY MMM DD'
        
        ws['A9'] = 'Состоит больных'
        ws['E9'] = svod.vsego


        ws['A10'] = 'В т.ч. детей'
        ws['E10'] = svod.child

        ws['A11'] = 'Всего матерей по уходу'
        ws['E11'] = svod.mam

        ws['A12'] = 'Из них без питания'
        ws['E12'] = svod.mam_nofood

        ws['A13'] = 'Ветераны УВОВ'
        ws['E13'] = svod.wow
        wb.save(f"{d}.xlsx")
    except:
        print("ошибка при формировании отчета")

