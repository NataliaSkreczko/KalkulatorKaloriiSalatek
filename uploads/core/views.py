
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from scipy import stats


import csv
import pandas as pd

def about(request):
    print('About')
    return render(request, 'about.html')

def contact(request):
    print('Contact')
    return render(request, 'contact.html')

def home(request):
    print('Home')
    return render(request, 'home.html')


def data_analysis(request):
    if request.method == 'POST':
        try:
            for i in request.POST:
                print(i)
            if 'tomatocheckbox' in request.POST:
                tomato = int(request.POST['tomato'])
                tomato *=18/100
                tomato=round(tomato,3)
            else:
                tomato = 0
            if 'saladcheckbox' in request.POST:
                salad = round(int(request.POST['salad']),3)
                salad *=18/100
                salad=round(salad,3)
            else:
                salad = 0
            if 'picklecheckbox' in request.POST:
                pickle = round(int(request.POST['pickle']),3)
                pickle *=18/100
                pickle=round(pickle,3)
            else:
                pickle = 0
            if 'iceberg_lettucecheckbox' in request.POST:
                iceberg_lettuce = round(int(request.POST['iceberg_lettuce']),3)
                iceberg_lettuce *=14/100
                iceberg_lettuce=round(iceberg_lettuce,3)
            else:
                iceberg_lettuce = 0
            if 'rucolacheckbox' in request.POST:
                rucola = round(int(request.POST['rucola']),3)
                rucola *=25/100
                rucola=round(rucola,3)
            else:
                rucola = 0
            if 'corn_saladcheckbox' in request.POST:
                corn_salad = round(int(request.POST['corn_salad']),3)
                corn_salad *=21/100
                corn_salad=round(corn_salad,3)
            else:
                corn_salad = 0
            if 'chinese_cabbagecheckbox' in request.POST:
                chinese_cabbage = round(int(request.POST['chinese_cabbage']),3)
                chinese_cabbage *=12/100
                chinese_cabbage=round(chinese_cabbage,3)
            else:
                chinese_cabbage = 0
            if 'romaine_lettucecheckbox' in request.POST:
                romaine_lettuce = round(int(request.POST['romaine_lettuce']),3)
                romaine_lettuce *=17/100
                romaine_lettuce=round(romaine_lettuce,3)
            else:
                romaine_lettuce = 0
            if 'raspberry_tomatocheckbox' in request.POST:
                raspberry_tomato = round(int(request.POST['raspberry_tomato']),3)
                raspberry_tomato *=18/100
                raspberry_tomato=round(raspberry_tomato,3)
            else:
                raspberry_tomato = 0
            if 'cherry_tomatocheckbox' in request.POST:
                cherry_tomato = round(int(request.POST['cherry_tomato']),3)
                cherry_tomato *=19/100
                cherry_tomato=round(cherry_tomato,3)
            else:
                cherry_tomato = 0
            if 'red_peppercheckbox' in request.POST:
                red_pepper = round(int(request.POST['red_pepper']),3)
                red_pepper *=40/100
                red_pepper=round(red_pepper,3)
            else:
                red_pepper = 0
            if 'yellow_peppercheckbox' in request.POST:
                yellow_pepper = round(int(request.POST['yellow_pepper']),3)
                yellow_pepper *=27/100
                yellow_pepper=round(yellow_pepper,3)
            else:
                yellow_pepper = 0
            if 'green_peppercheckbox' in request.POST:
                green_pepper = round(int(request.POST['green_pepper']),3)
                green_pepper *=18/100
                green_pepper=round(green_pepper,3)
            else:
                green_pepper=0
            if 'carrotcheckbox' in request.POST:
                carrot = int(request.POST['carrot'])
                carrot *=27/100
                carrot=round(carrot,3)
            else:
                carrot = 0
            if 'parmesancheckbox' in request.POST:
                parmesan = int(request.POST['parmesan'])
                parmesan *=392/100
                parmesan=round(parmesan,3)
            else:
                parmesan = 0
            if 'olivecheckbox' in request.POST:
                olive = int(request.POST['olive'])
                olive *=884/100
                olive=round(olive,3)
            else:
                olive = 0

            summary = tomato + salad + pickle + iceberg_lettuce + rucola + corn_salad + chinese_cabbage + romaine_lettuce + raspberry_tomato + cherry_tomato + red_pepper + yellow_pepper + green_pepper + carrot + olive + parmesan
            return render(request, 'data_analysis.html',
                        {'result_present': True,
                        'tomato': tomato,
                        'salad': salad,
                        'pickle': pickle,
                        'iceberg_lettuce' : iceberg_lettuce,
                        'rucola' : rucola,
                        'corn_salad' : corn_salad,
                        'chinese_cabbage' : chinese_cabbage,
                        'romaine_lettuce' : romaine_lettuce,
                        'raspberry_tomato' : raspberry_tomato,
                        'cherry_tomato' : cherry_tomato,
                        'red_pepper' : red_pepper,
                        'yellow_pepper' : yellow_pepper,
                        'green_pepper' : green_pepper,
                        'carrot' : carrot,
                        'parmesan' : parmesan,
                        'olive' : olive,
                        'summary': summary,
                        'error':""})
        except ValueError:
            tomato = 0
            salad = 0
            pickle = 0
            iceberg_lettuce = 0
            rucola = 0
            corn_salad = 0
            chinese_cabbage = 0
            romaine_lettuce = 0
            raspberry_tomato = 0
            cherry_tomato = 0
            red_pepper = 0
            yellow_pepper = 0
            green_pepper = 0
            carrot = 0
            parmesan = 0
            olive = 0
            summary = 0
            error = "Wprowadzono niepoprawne dane. Spróbuj jeszcze raz."
            return render(request, 'data_analysis.html',
                        {'result_present': True,
                        'tomato': tomato,
                        'salad': salad,
                        'pickle': pickle,
                        'iceberg_lettuce' : iceberg_lettuce,
                        'rucola' : rucola,
                        'corn_salad' : corn_salad,
                        'chinese_cabbage' : chinese_cabbage,
                        'romaine_lettuce' : romaine_lettuce,
                        'raspberry_tomato' : raspberry_tomato,
                        'cherry_tomato' : cherry_tomato,
                        'red_pepper' : red_pepper,
                        'yellow_pepper' : yellow_pepper,
                        'green_pepper' : green_pepper,
                        'carrot' : carrot,
                        'parmesan' : parmesan,
                        'olive' : olive,
                        'summary': summary,
                        'error':error})
    return render(request, 'data_analysis.html')
