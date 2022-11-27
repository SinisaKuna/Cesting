import pyodbc
drivers = [item for item in pyodbc.drivers()]
print(drivers)
for driver in drivers:
    print(driver)
    if 'SQL Server' in driver:
        useDriver = driver 
