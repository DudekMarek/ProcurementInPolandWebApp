import locale
import requests
from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/dane-o-zamowieniach')
def procurments():
    #Pobieranie danych z API i formatowanie 
    allData = requests.get('https://tenders.guru/api/pl/tenders').json()

    #Wyciąganie z całego pliku JSON listy obiektów opisujących poszczególne zamówienia
    data = allData['data']
    for proc in data:
        proc['awarded_value_eur'] = format_number(proc['awarded_value_eur'])
        
    return render_template('procurment.html', data=data)

#Funkcja służąca do formatowanie liczb w celu łatwiejszego ich czytania
def format_number(num_str):
    locale.setlocale(locale.LC_ALL, ('pl_PL', 'UTF-8'))

    num = float(num_str)

    formated_num = locale.format_string("%.2f", num, grouping=True)
    
    
    return formated_num