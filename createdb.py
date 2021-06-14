# importing library
import pandas as pd
import csv
import sqlite3

try:
  
    # Import csv and extract data
    df = pd.read_csv('./database_file/FIPSCode.csv')


    df.to_csv (r'./database_file/counties.csv', index = False, header=True)


    # Import csv and extract data
    with open('./database_file/counties.csv', 'r') as fin:
            dr = csv.DictReader(fin)
            county_info = [(i['CODE'],i['NAME'], i['STATE']) for i in dr]
            #print(county_info)

    # Connect to SQLite
    sqliteConnection = sqlite3.connect('./database_file/counties.db')
    cursor = sqliteConnection.cursor()

    # check if table exists
    print('Check if Counties table exists in the database:')
    listOfTables = cursor.execute(
    """SELECT Name FROM sqlite_master WHERE type='table'
    AND Name='counties'; """).fetchall()

    if listOfTables == []:
        print('Table not found!')
    else:
        cursor.execute('DROP TABLE IF EXISTS counties')

    print(county_info)
    # Create student table
    cursor.execute('create table counties(fipscode int, name varchar2(50), state varchar2(2));')

    # Insert data into table
    cursor.executemany(
        "insert into counties (fipscode,name,state) VALUES (?, ?, ?);", county_info)

    # Show counties table
    cursor.execute('select * from counties;')

    # View result
    result = cursor.fetchall()
    print(result)

    # Commit work and close connection
    sqliteConnection.commit()
    cursor.close()

except sqlite3.Error as error:
    print('Error occured - ', error)

finally:
   if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed')





try:
  
    # Import csv and extract data
    state_df = pd.read_csv('./database_file/states.csv')


    state_df.to_csv (r'./database_file/cleanstates.csv', index = False, header=True)


    # Import csv and extract data
    with open('./database_file/cleanstates.csv', 'r') as fin:
            dr = csv.DictReader(fin)
            state_info = [(i['NAME'], i['ABBR']) for i in dr]
            #print(county_info)

    # Connect to SQLite
    sqliteConnection = sqlite3.connect('./database_file/counties.db')
    cursor = sqliteConnection.cursor()

    # check if table exists
    print('Check if states table exists in the database:')
    listOfTables = cursor.execute(
    """SELECT Name FROM sqlite_master WHERE type='table'
    AND Name='states'; """).fetchall()

    if listOfTables == []:
        print('Table not found!')
    else:
        cursor.execute('DROP TABLE IF EXISTS states')

    print(state_info)
    # Create student table
    cursor.execute('create table states(name varchar2(50), abbr varchar2(2));')

    # Insert data into table
    cursor.executemany(
        "insert into states (name,abbr) VALUES (?, ?);", state_info)

    # Show counties table
    cursor.execute('select * from states;')

    # View result
    result = cursor.fetchall()

    # Commit work and close connection
    sqliteConnection.commit()
    cursor.close()

except sqlite3.Error as error:
   print('Error occured - ', error)

finally:
   if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed')


try:
    
    # Import csv and extract data
    state_df = pd.read_csv('./database_file/EPA_City_2020.csv')
    state_df.to_csv (r'./database_file/epa2020.csv', index = False, header=True)

    # Import csv and extract data
    with open('./database_file/epa2020.csv', 'r') as fin:
            dr = csv.DictReader(fin)
            epa_info = [(i['State'], i['County'],i['County FIPS Code'],i['2010 Population'],i['CO 8-hr'],i['Pb 3-mo'],i['NO2 AM'],i['NO2 1-hr'],i['O3 8hr'],i['PM10 24-hr'],i['PM2.5 Wtd'],i['PM2.5 24-hr'],i['SO2 1-hr']) for i in dr]
            #print(county_info)

    # Connect to SQLite
    sqliteConnection = sqlite3.connect('./database_file/counties.db')
    cursor = sqliteConnection.cursor()

    # check if table exists
    print('Check if states table exists in the database:')
    listOfTables = cursor.execute("""SELECT Name FROM sqlite_master WHERE type='table' AND Name='epa'; """).fetchall()

    if listOfTables == []:
        print('Table not found!')
    else:
        cursor.execute('DROP TABLE IF EXISTS epa')

    print(state_info)
    # Create epa table
    cursor.execute('create table epa(state varchar2(50), county varchar2(50), fipcode int, population int, CO_8hr int, PB_3mo decimal, NO2_AM int, NO2_1hr int, O3_8hr decimal, PM10_24hr int, PM25_Wtd_AM decimal, PM25_24hr int, SO2_1hr int);')

    # Insert data into table
    cursor.executemany(
        "insert into epa (state, county, fipcode, population, CO_8hr, PB_3mo, NO2_AM, NO2_1hr, O3_8hr, PM10_24hr,PM25_Wtd_AM, PM25_24hr, SO2_1hr) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", epa_info)

    # Show counties table
    cursor.execute('select * from epa;')

    # View result
    result = cursor.fetchall()

    # Commit work and close connection
    sqliteConnection.commit()
    cursor.close()

except sqlite3.Error as error:
     print('Error occured - ', error)

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed')


try:
  
    # Import csv and extract data
    df = pd.read_csv('./database_file/covidbystatefromcsv.csv')

    # Import csv and extract data
    with open('./database_file/covidbystatefromcsv.csv', 'r') as fin:
            dr = csv.DictReader(fin)
            covidbystate_info = [(i['fips'],i['country'], i['state'], i['county'], i['population'], i['PositivityRatio'], i['Density'], i['ActualCases'], i['ActualDeaths'], i['ActualHospitalBedCapacity'],i['ActualHospitalBedCurrentUsageTotal'], i['ActualHospitalBedCurrentUsageCovid'],i['ActualHospitalBedTypicalUsageRate'],i['ActualIcuBedsCapacity'],i['ActualIcuBedCurrentUsageTotal'],i['ActualIcuBedCurrentUsageCovid'],i['ActualIcuBedTypicalUsageRate'],i['ActualNewCases'],i['ActualVaccinationInitiated'],i['ActualVaccinationCompleted'],i['VaccinationInitaitedRatio'],i['VaccinationCompletedRatio'],i['ActualNewDeaths'],i['ActualVaccinesAdministered']) for i in dr]
            #print(county_info)

    # Connect to SQLite
    sqliteConnection = sqlite3.connect('./database_file/counties.db')
    cursor = sqliteConnection.cursor()

    # check if table exists
    print('Check if covidbystate table exists in the database:')
    listOfTables = cursor.execute(
    """SELECT Name FROM sqlite_master WHERE type='table'
    AND Name='covidbystate'; """).fetchall()

    if listOfTables == []:
        print('Table not found!')
    else:
        cursor.execute('DROP TABLE IF EXISTS covidbystate')
    
    # Create covidbystate table
    cursor.execute('create table covidbystate(fips int ,country varchar(50),state varchar(50),county varchar(50),population int,PositivityRatio decimal,Density decimal,ActualCases int,ActualDeaths int,ActualHospitalBedCapacity int,ActualHospitalBedCurrentUsageTotal int,ActualHospitalBedCurrentUsageCovid int,ActualHospitalBedTypicalUsageRate decimal,ActualIcuBedsCapacity int ,ActualIcuBedCurrentUsageTotal int,ActualIcuBedCurrentUsageCovid int,ActualIcuBedTypicalUsageRate decimal,ActualNewCases int,ActualVaccinationInitiated int,ActualVaccinationCompleted int,VaccinationInitaitedRatio decimal,VaccinationCompletedRatio decimal,ActualNewDeaths int,ActualVaccinesAdministered int);')

    # Insert data into table
    cursor.executemany("insert into covidbystate (fips,country,state,county,population,PositivityRatio,Density,ActualCases,ActualDeaths,ActualHospitalBedCapacity,ActualHospitalBedCurrentUsageTotal,ActualHospitalBedCurrentUsageCovid,ActualHospitalBedTypicalUsageRate,ActualIcuBedsCapacity,ActualIcuBedCurrentUsageTotal,ActualIcuBedCurrentUsageCovid,ActualIcuBedTypicalUsageRate,ActualNewCases,ActualVaccinationInitiated,ActualVaccinationCompleted,VaccinationInitaitedRatio,VaccinationCompletedRatio,ActualNewDeaths,ActualVaccinesAdministered) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", covidbystate_info)

    # Show counties table
    cursor.execute('select * from covidbystate;')

    # View result
    result = cursor.fetchall()
    print(result)

    # Commit work and close connection
    sqliteConnection.commit()
    cursor.close()

except sqlite3.Error as error:
    print('Error occured - ', error)

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed')        