
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

from openpyxl.styles import  Alignment,  Font, Border, Side


from datetime import date
# Create your views here.
def login(request: HttpRequest):

    if(request.COOKIES.get('otd')):
        return redirect('main')

    if (request.POST):

        if (request.POST['itotd'] == 'nmb1'):
            response = redirect('main')
            response.set_cookie('otd','nmb1', max_age=60 * 120)
            return response
            

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

    if (otd_id == 'nmb1'):
        context = {
            'otd': 0
        }
        return render(request, 'app/main.html', context=context)

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
    if (otd_id == 'nmb1'):
        return render(request, 'app/food_svod.html')


    otd = Otd.objects.get(idotd = otd_id)
    
    context = {
        'otd': otd
    }
    return render(request, 'app/food_svod.html', context=context)


def get_svod_by_date(request: HttpRequest, year: int, month: int, day:int):
    start_datetime = datetime.datetime(year=year, month=month, day=day)
    delta_tm = datetime.timedelta(hours=23, minutes=59, seconds=58)
    end_datetime = start_datetime + delta_tm

    print(datetime.datetime.today())

    # для админа
    if (request.COOKIES.get('otd') == 'nmb1'):
        otd_id = request.COOKIES.get('otd')
        svod = Food_svod.objects.filter(
            dt_svood__range = (start_datetime, end_datetime)
        )
        return JsonResponse({
            'length': svod.count(),
            'svod': serializers.serialize('json', svod)
        })

    #для отделений
    otd_id = request.COOKIES.get('otd')
    svod = Otd.objects.get(pk=otd_id)
    result = svod.food_svod_set.filter(
        dt_svood__range = (start_datetime, end_datetime)
    )

    print(start_datetime.isoformat())
    print(end_datetime.isoformat())

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
    value = request.POST['value']
    otd_id = request.COOKIES.get('otd')

    dt = datetime.datetime.strptime(time,  "%Y-%m-%d %H:%M:%S")
    if (otd_id == 'nmb1'):
        id = int(request.POST['otd_id'])
        svod = Food_svod.objects.get(idotd_id=id, dt_svood__icontains=dt)
    else:
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
    if column == 'diet_age_1_3':
        svod.diet_age_1_3 = value
    if column == 'diet_age_3_7':
        svod.diet_age_3_7 = value
    if column == 'diet_age_7_11':
        svod.diet_age_7_11 = value
    if column == 'diet_age_11_18':
        svod.diet_age_11_18 = value
    
    svod.save()


    return JsonResponse({'otd': serializers.serialize('json', [svod, ])})
    

def create_new_food_svod(request: HttpRequest):
    if(request.COOKIES.get('otd') == None):
        return redirect('login')
    otd = Otd.objects.get(pk=request.COOKIES.get('otd'))
    new_food_svod = otd.food_svod_set.create()


    return JsonResponse({
        'svod': serializers.serialize('json', [new_food_svod, ])
    })



def report(request: HttpRequest, datetm:str ):

    if(request.COOKIES.get('otd') == None):
        return redirect('login')
    print(datetm)
    start_datetime = datetime.datetime.fromisoformat(datetm)
    delta_td = datetime.timedelta(hours=23, minutes=59, seconds=58)
    end_datetime = start_datetime + delta_td


    if (request.COOKIES.get('otd') != 'nmb1'):
        otd_id = Otd.objects.get(pk=request.COOKIES.get('otd'))

        svod = Food_svod.objects.get(idotd_id=otd_id, 
        dt_svood__range = (start_datetime, end_datetime)               
        )
        create_report_seven(otd_id, svod, start_datetime.date(), "СВОДКА ПИТАНИЯ")
        return JsonResponse({
            'message': 'success'
        })
    else:
        svod_for_all_otd = Food_svod.objects.filter(
            dt_svood__range  =(start_datetime, end_datetime)
        )
        print(svod_for_all_otd.count())
        create_report_for_all_otd(svod_for_all_otd, start_datetime.date())
        return JsonResponse({
            'message': 'success'
        })



    


def create_report_for_all_otd(svod, d: date):
    print(timezone.datetime.today())
    right_alignment = Alignment(
        horizontal='right'
    )
    font_6 = Font(
        size= 6
    )
    font_9 = Font(
        size= 9
    )

    font_7 = Font(
        size=7,
    )

    border = Border(
        bottom=Side(border_style="thin",
                    color='FF000000')
    )

    side = Side(border_style="thin",
        color='FF000000')
    
    around_Border = Border(
        left=side,
        right=side,
        bottom=side,
        top=side
    )


    left_border = Border( left=side )
    right_border = Border(right=side)
    top_border = Border(top=side)
    bottom_border = Border(bottom=side)
   
    wb = Workbook()
    ws = wb.active

    #меняем шрифт
    for i in range(1, 15):
        for j in range(1,100):
            cell = ws.cell(row=j, column=i)
            cell.font = Font(name='Arial')

    ws['N1'] = 'Форма №22-M3'
    ws['N1'].alignment = right_alignment
    ws['N2'] = 'к Инструкции по организации лечебного питания'
    ws['N2'].alignment = right_alignment
    ws['N3'] = 'в лечебно-проф.учреждениях КГБУЗ "НМБ №1"'
    ws['N3'].alignment = right_alignment


    for k in range(0, 6):
        for i in range(1, 6):
            cell = ws.cell(row=8+k, column=i)
            cell.border = border

    ws['A4'] = 'Сводка Питания'
    
    ws['A5'] = "На 7:00"
    cell = ws['E8']
    cell.value = d
    cell.number_format = 'yyyy-mm-dd'
    
    ws['A6'] = 'Состоит больных'
    ws['E9'] = f"=SUM(B15:B{14 + len(svod)})"

    ws['A7'] = 'В т.ч. детей'
    #ws['E10'] = child

    ws['A8'] = 'Всего матерей по уходу'
    #ws['E11'] = mam

    ws['A9'] = 'Из них без питания'
    #ws['E12'] = mam_nofood

    ws['A10'] = 'Ветераны УВОВ'
    #ws['E13'] = wow

    ws.merge_cells('A12:A14')
    ws['A12'].value = "ОТД"
    ws['A12'].border = around_Border
    ws['A13'].border = around_Border
    ws['B12'].border = around_Border
    ws['B13'].border = around_Border
    ws['C13'].border = around_Border
    ws['D13'].border = around_Border
    ws['E13'].border = around_Border
    ws['F13'].border = around_Border
    ws['G13'].border = around_Border
    ws['H13'].border = around_Border
    ws['I13'].border = around_Border
    ws['J13'].border = around_Border
    ws['K13'].border = around_Border
    ws['L13'].border = around_Border
    ws['M13'].border = around_Border
    ws['N13'].border = around_Border

    ws['A14'].border = around_Border
    ws['B14'].border = around_Border
    ws['B14'].border = around_Border
    ws['C14'].border = around_Border
    ws['D14'].border = around_Border
    ws['E14'].border = around_Border
    ws['F14'].border = around_Border
    ws['G14'].border = around_Border
    ws['H14'].border = around_Border
    ws['I14'].border = around_Border
    ws['J14'].border = around_Border
    ws['K14'].border = around_Border
    ws['L14'].border = around_Border
    ws['M14'].border = around_Border
    ws['N14'].border = around_Border

    ws.merge_cells('B12:B14')
    ws['B12'].value = "кол-во больных"

    ws.merge_cells('C12:N12')
    ws['C12'].value = 'СТАНДАРТНЫЕ ДИЕТЫ ( СТОЛЫ )'
    ws['C12'].font = font_7


    ws.merge_cells('C13:C14')
    ws['C13'].value = 'ЗОНД'

    ws.merge_cells('D13:D14')
    ws['D13'].value = 'ГОЛОД'

    ws.merge_cells('E13:F13')
    ws['E13'].value = '01'

    ws['E14'].value =  'Кисель'
    ws['F14'].value =  'Бульон'
    
    ws.merge_cells('G13:G14')
    ws['G13'].value = '02'

    ws.merge_cells('H13:H14')
    ws['H13'].value = '03'

    ws.merge_cells('I13:I14')
    ws['I13'].value = 'ОВД'

    ws.merge_cells('J13:J14')
    ws['J13'].value = 'ЩД'

    ws.merge_cells('K13:K14')
    ws['K13'].value = 'Д'

    ws.merge_cells('L13:L14')
    ws['L13'].value = 'ВБД'

    ws.merge_cells('M13:M14')
    ws['M13'].value = 'НБД'

    

    ws.merge_cells('N13:N14')
    ws['N13'].value = 'НКД'
    columns = 'ABCDEFGHIJKLMN'
    for i in range(0, len(svod)):
        if (i  < len(svod)):
            ws.insert_rows(15)
        item = svod[i]
        ws['A15'] = item.idotd.short_otd
        ws['B15'] = item.vsego
        ws['C15'] = item.zond
        ws['D15'] = item.golod
        ws['E15'] = item.diet_01_kis
        ws['F15'] = item.diet_01_bul
        ws['G15'] = item.diet_02
        ws['H15'] = item.diet_03
        ws['I15'] = item.diet_ovd
        ws['J15'] = item.diet_shd
        ws['K15'] = item.diet_child
        ws['L15'] = item.diet_vdb
        ws['M15'] = item.diet_nbd
        ws['N15'] = item.diet_nkd

        
    ws["B42"] = f"=SUM(B15:B{14 + len(svod)})"

    


    # ws.row_dimensions[18].height = 25
    # ws.row_dimensions[16].alignment = Alignment(vertical='center')
    # ws.row_dimensions[17].alignment = Alignment(vertical='center')
    # ws.row_dimensions[18].alignment = Alignment(vertical='center')

    # ws.row_dimensions[16].font = Font(size=7)
    # ws.row_dimensions[17].font = Font(size=7)
    # ws.row_dimensions[18].font = Font(size=7)
    


    # #полная граница граница сводки  [A15:N18]
    for i in range(1, 15):
        for j in range(1, len(svod) + 2):
            cell = ws.cell(row=14 + j, column=i)
            cell.border = around_Border
            cell.font = font_7




    #задаем ширину столбца
    for i in range(0, 14):
        columns = 'ABCDEFGHIJKLMN'
        
        row = ws.column_dimensions[columns[i]]
        row.width = 5.43 +  0.67

    for i in range(1, 4):
        ws.row_dimensions[i].height = 9

    for i in range(6, 42):
        ws.row_dimensions[i].height = 12

            #меняем шрифт
    for i in range(1, 15):
        for j in range(1,100):
            cell = ws.cell(row=j, column=i)
            cell.font = Font(name='Arial', size=7)
            
    for i in range(5, 11):
        ws[f"A{i}"].font = Font(name='Arial')

    ws['A5'].font = Font(size=9)
    ws['A6'].font = Font(size=9)
    ws['A7'].font = Font(size=9)
    ws['A8'].font = Font(size=9)
    ws['A9'].font = Font(size=9)
    ws['A10'].font = Font(size=9)
    ws['N1'].font = font_6
    ws['N2'].font = font_6
    ws['N3'].font = font_6


    filename = datetime.datetime.now().strftime("%m-%d-%Y %H.%M.%S")
    wb.save(f"{filename}.xlsx")












def create_report_seven(otd: Otd, svod: Food_svod, d: date, title:str):
    right_alignment = Alignment(
        horizontal='right'
    )
    font_6 = Font(
        size= 6
    )
    font_9 = Font(
        size= 9
    )

    border = Border(
        bottom=Side(border_style="thin",
                    color='FF000000')
    )

    side = Side(border_style="thin",
        color='FF000000')
    
    around_Border = Border(
        left=side,
        right=side,
        bottom=side,
        top=side
    )


    left_border = Border( left=side )
    right_border = Border(right=side)
    top_border = Border(top=side)
    bottom_border = Border(bottom=side)
   
    wb = Workbook()
    ws = wb.active

    #меняем шрифт
    for i in range(1, 15):
        for j in range(1,100):
            cell = ws.cell(row=j, column=i)
            cell.font = Font(name='Arial')
        
    

    ws['N1'] = 'Форма №1-84'
    ws['N1'].alignment = right_alignment
    ws['N1'].font = font_6
    ws['N2'] = 'к Инструкции по организации лечебного питания'
    ws['N2'].alignment = right_alignment
    ws['N2'].font = font_6
    ws['N3'] = 'в лечебно-проф.учреждениях КГБУЗ "НМБ №1"'
    ws['N3'].alignment = right_alignment
    ws['N3'].font = font_6
    ws['A4'] = title
    ws['A4'].font = font_9

    for k in range(0, 6):
        for i in range(1, 6):
            cell = ws.cell(row=8+k, column=i)
            cell.border = border

    ws['N6'].value = otd.otd_name
    ws['N6'].alignment = right_alignment
    ws['N6'].font = Font(
        size = 14
    )

    
    ws['A8'] = "На 7:00"
    cell = ws['E5']
    cell.value = d
    cell.number_format = 'yyyy-mm-dd'
    
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

    ws.merge_cells('A15:A17')
    ws['A15'].value = "ОТД"


    ws.merge_cells('B15:B17')
    ws['B15'].value = "кол-во больных"

    ws.merge_cells('C15:N15')
    ws['C15'].value = 'СТАНДАРТНЫЕ ДИЕТЫ ( СТОЛЫ )'
    ws.merge_cells('C16:C17')
    ws['C16'].value = 'ЗОНД'

    ws.merge_cells('D16:D17')
    ws['D16'].value = 'ГОЛОД'

    ws.merge_cells('E16:F16')
    ws['E16'].value = '01'

    ws['E17'].value =  'Кисель'
    ws['F17'].value =  'Бульон'
    
    ws.merge_cells('G16:G17')
    ws['G16'].value = '02'

    ws.merge_cells('H16:H17')
    ws['H16'].value = '03'

    ws.merge_cells('I16:I17')
    ws['I16'].value = 'ОВД'

    ws.merge_cells('J16:J17')
    ws['J16'].value = 'ЩД'

    ws.merge_cells('K16:K17')
    ws['K16'].value = 'Д'

    ws.merge_cells('L16:L17')
    ws['L16'].value = 'ВБД'

    ws.merge_cells('M16:M17')
    ws['M16'].value = 'НБД'

    ws.merge_cells('N16:N17')
    ws['N16'].value = 'НКД'


    ws.row_dimensions[18].height = 25
    ws.row_dimensions[16].alignment = Alignment(vertical='center')
    ws.row_dimensions[17].alignment = Alignment(vertical='center')
    ws.row_dimensions[18].alignment = Alignment(vertical='center')

    ws.row_dimensions[16].font = Font(size=7)
    ws.row_dimensions[17].font = Font(size=7)
    ws.row_dimensions[18].font = Font(size=7)
    
    ws['A18'].value = otd.short_otd
    ws['B18'].value = svod.vsego
    ws['C18'].value = svod.zond
    ws['D18'].value = svod.golod
    ws['E18'].value = svod.diet_01_kis
    ws['F18'].value = svod.diet_01_bul
    ws['G18'].value = svod.diet_02
    ws['H18'].value = svod.diet_03
    ws['I18'].value = svod.diet_ovd
    ws['J18'].value = svod.diet_shd
    ws['K18'].value = svod.diet_child
    ws['L18'].value = svod.diet_vdb
    ws['M18'].value = svod.diet_nbd
    ws['N18'].value = svod.diet_nkd
    

    ws['A27'].value = 'Зав.отделением'
    ws['A28'].value = 'Ст.мед.сестра'
    ws['A29'].value = 'Дежурная мед.сестра'

    ws['E27'].value = otd.zav_otd
    ws['E28'].value = otd.msister
    ws['E29'].value = svod.fio_ms

    #полная граница граница сводки  [A15:N18]
    for i in range(1, 15):
        for j in range(1, 5):
            cell = ws.cell(row=14 + j, column=i)
            cell.border = around_Border

    for i in range(1,15):
        cell = ws.cell(row=33, column=i)
        cell.border = bottom_border


    #задаем ширину столбца
    for i in range(0, 14):
        columns = 'ABCDEFGHIJKLMN'
        
        row = ws.column_dimensions[columns[i]]
        row.width = 5.43 +  0.67

    wb.save(f"{d}.xlsx")




def set_full_border(cells):
    side = Side(border_style="thin",
        color='FF000000')
    
    around_Border = Border(
        left=side,
        right=side,
        bottom=side,
        top=side
    )
    for cell in cells:
        cell.border = around_Border