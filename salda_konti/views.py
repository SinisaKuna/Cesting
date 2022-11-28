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
# import pyodbc
# import pymssql
import mysql.connector


def connect_database():
    # # # *** CESTING SERVER ***
    # server = '213.202.107.109,1433'
    # database = data_base    
    # username = 'sa'
    # password = '@betaStudio2017'
    # # conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)
    # conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)
    conn = mysql.connector.connect(
        host="178.218.166.150",
        user="betastudio_sa",
        password="@korisnik",
        database="betastudio_dbbetasoft"
    )
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
    conn = connect_database()
    cursor = conn.cursor()
    query = "select sifra, naziv, duguje from kupci"
    cursor.execute(query)
    result = cursor.fetchall()
    return render(request, "salda_konti_kupci.html", {'SaldaKonti': result})


def rang_lista_dobavljaci(request):
    conn = connect_database()
    cursor = conn.cursor()
    query = "select sifra, naziv, potrazuje from dobavljaci"
    cursor.execute(query)
    result = cursor.fetchall()
    return render(request, "salda_konti_dobavljaci.html", {'SaldaKonti': result})


def analiza_prosjeka_place(request): 
    conn = connect_database()
    cursor = conn.cursor()
    query = "select * from prosjek_place"
    cursor.execute(query)
    result = cursor.fetchall()
    return render(request, "analiza_prosjeka_place.html", {'AnalizaPlace': result})
    

def test_konekcije(request):    
    return render(request, "index.html")
