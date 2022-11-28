import pyodbc
# import pymssql
import mysql.connector

def connect_database():
    conn = mysql.connector.connect(
        host="178.218.166.150",
        user="betastudio_sa",
        password="@korisnik",
        database="betastudio_dbbetasoft"
    )
    return conn

conn = connect_database()
cursor = conn.cursor()
query = "select sifra, naziv, duguje from kupci"
cursor.execute(query)
result = cursor.fetchall()
for x in result:
    print(x[0])

print("\n///\n")

def connect_cesting(data_base):
    # # *** CESTING SERVER ***
    server = '213.202.107.109,1433'
    database = data_base
    username = 'sa'
    password = '@betaStudio2017'
    conn = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER=' +
                          server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD=' + password)
    return conn 

conn = connect_cesting('cesting_2022')
cursor = conn.cursor()
query = "select sifra, naziv, duguje from web_rang_lista_1200 where dug != 0 order by dug desc"
cursor.execute(query)
sql_result = cursor.fetchall()
for x in sql_result:
    print(x.sifra)
  