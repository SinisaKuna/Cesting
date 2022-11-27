from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from cesting import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout
from .models import SaldaKonti
import pyodbc


def connect_database(data_base):
    
    # # *** WORK\DBBETASOFT SERVER ***
    # server = 'WORK\DBBETASOFT'    
    # # server = 'WORK\SQLEXPRESS12'       
    # # server = 'WORK\SQLEXPRESS14'   
    # database = data_base
    # username = 'sa'
    # password = '@betaStudio2017'
    # conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE=' + database+';ENCRYPT=no;UID='+username+';PWD=' + password)
    # conn = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)
    # conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)
    # conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)
    
    # conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)
    # conn = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)
    # conn = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)

    # # *** CESTING SERVER ***
    server = '213.202.107.109,1433'
    database = data_base    
    username = 'sa'
    password = '@betaStudio2017'
    # ne radi na Cesting serveru
    # # conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)

    # # ovi rade
    # # conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)    
    # # conn = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)
    # # conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)
    # conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)    
    conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)
    
    return conn


def home(request):    
    # --- ISPISUJE DRIVERE ZA SPAJANJE SA SQL SERVEROM
    # messages.error(request, "Instalirani driveri:")
    # messages.error(request, "---")
    # drivers = [item for item in pyodbc.drivers()]
    # for driver in drivers:
    #     messages.error(request, driver)
    # messages.error(request, "---")
    # ---
    return render(request, "index.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            fname = user.first_name
            return redirect('home')
        else:
            messages.error(
                request, "Nepoznat korisnik ili račun nije aktivan!")
            return redirect('home')
    return render(request, "signin.html")


def signout(request):
    logout(request)
    user = authenticate(username="", password="")
    messages.success(request, "Uspješno ste odjavljeni!")
    return redirect('home')


def rang_lista_kupci(request):
    conn = connect_database('cesting_2022')
    cursor = conn.cursor()
    query = "select * from web_rang_lista_1200 order by dug desc"
    cursor.execute(query)
    result = cursor.fetchall()
    return render(request, "salda_konti_kupci.html", {'SaldaKonti': result})


def rang_lista_dobavljaci(request):
    conn = connect_database('cesting_2022')
    cursor = conn.cursor()
    query = "select * from web_rang_lista_2200 order by pot desc"
    cursor.execute(query)
    result = cursor.fetchall()
    return render(request, "salda_konti_dobavljaci.html", {'SaldaKonti': result})


def analiza_prosjeka_place(request): 
    conn = connect_database('placa_0000')
    cursor = conn.cursor()
    query = "select * from web_analiza_prosjeka_primanja order by prezime_ime"
    cursor.execute(query)
    result = cursor.fetchall()
    return render(request, "analiza_prosjeka_place.html", {'AnalizaPlace': result})
