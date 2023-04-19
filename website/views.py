import locale
import requests
from flask import Blueprint, render_template, request

views = Blueprint("views", __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/dane-o-zamowieniach', methods=['GET', 'POST'])
def procurments():
    url = 'https://tenders.guru/api/pl/tenders'
    
    # Obsługa przechodzenia na kolejne strony
    if request.method == 'POST':
        page = request.form.get('page')
        params = {"page": f"{page}"}
        allData = requests.get(url, params=params).json()
        
    # Obsługa przejścia na pierwszą stronę
    else:
        allData = requests.get(url).json()
    
    
    currentPage = allData['page_number']
        
    #Wyciąganie z całego pliku JSON listy obiektów opisujących poszczególne zamówienia
    data = allData['data']
    for proc in data:
        proc['awarded_value_eur'] = format_number(proc['awarded_value_eur'])
    
        
    return render_template('procurment.html', data=data, currentPage=currentPage)

#Funkcja służąca do formatowanie liczb w celu łatwiejszego ich czytania
def format_number(num_str):
    locale.setlocale(locale.LC_ALL, ('pl_PL', 'UTF-8'))

    num = float(num_str)

    formated_num = locale.format_string("%.2f", num, grouping=True)
    
    
    return formated_num

# Wyświetlanie szczegółów dotyczących zamówienia
@views.route('/detils/<int:id>')
def details(id):
    url = f'https://tenders.guru/api/pl/tenders/{id}'
    data = requests.get(url).json()
    data['awarded_value'] = format_number(data['awarded_value'])
    data['awarded_value_eur'] = format_number(data['awarded_value_eur'])
    
    return render_template('details.html', data=data)