
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
            if 'tomatocheckbox' in request.POST:
                tomato = int(request.POST['tomato'])
                tomato *=18/100
            else:
                tomato = 0
            salad = int(request.POST['salad'])
            pickle = int(request.POST['pickle'])
            salad *=15/100
            pickle *=10/100
            summary = tomato + salad + pickle
            return render(request, 'data_analysis.html',
                        {'result_present': True,
                        'tomato': tomato,
                        'salad': salad,
                        'pickle': pickle,
                        'summary': summary,
                        'error':""})
        except ValueError:
            tomato = 0
            salad = 0
            pickle = 0
            summary = 0
            error = "Bledne dane"
            return render(request, 'data_analysis.html',
                        {'result_present': True,
                        'tomato': tomato,
                        'salad': salad,
                        'pickle': pickle,
                        'summary': summary,
                        'error':error})
    return render(request, 'data_analysis.html')
