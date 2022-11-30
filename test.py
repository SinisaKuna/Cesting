import pyodbc
import mysql.connector

driver_list = ('SQL Server',
               'SQL Server Native Client 10.0',
               'SQL Server Native Client 11.0',
               'ODBC Driver 11 for SQL Server',
               'ODBC Driver 13 for SQL Server',
               'ODBC Driver 17 for SQL Server',
               'ODBC Driver 18 for SQL Server')


# *** CESTING SERVER ***
server = '213.202.107.109,1433'
database = "CESTING_2022"
username = 'sa'
password = '@betaStudio2017'
drivers = [item for item in pyodbc.drivers()]
driver = ""
for driver in drivers:
    if driver in driver_list:
        break
        
if driver != "":
    conn = pyodbc.connect('DRIVER={'+driver+'};SERVER=' +
                        server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD=' + password)
    print('DRIVER={'+driver+'};SERVER=' +
                        server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD=' + password)
else:
    print("Error")
    
cursor = conn.cursor()
query = "select sifra, naziv, duguje from web_rang_lista_1200 where dug != 0 order by dug desc"
cursor.execute(query)
result = cursor.fetchall()
for row in result:
    print(row)    
