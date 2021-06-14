from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
import pandas as pd
import csv
import sqlite3


# Import the requests library.
import requests

# Import the API key for Covid Act Now api's.
from config import can_key

from .models import Greeting
from database import list_counties, list_states, list_epa_by_state, list_model_data_by_state

# Create your views here.
def index(request):  
    #counties = list_counties()
    states= list_states()
    return render(request, "index.html", {"states" : states})

def dashboard(request):    
    return render(request, "dashboard.html")

def submitted(request): 
    #countySelected= request.POST.get('countyDropdown')
    stateSelected= request.POST.get('stateDropdown')
    #output = subprocess.check_call(['howdy.py'], shell=True)  
    stateurljson = "https://api.covidactnow.org/v2/county/" + stateSelected+ ".json?apiKey=" + can_key
    stateurlcsv = "https://api.covidactnow.org/v2/county/" + stateSelected + ".csv?apiKey=" + can_key
    stateepa = list_epa_by_state(stateSelected)

    try:
        covid_state_json = requests.get(stateurljson)
        covid_state = covid_state_json.text
        out_file = open("covid_by_state.json", "w").write(covid_state)
        out_file.close()

        

        
        
    except:
            print("COVID NOW state data not found. Skipping...")
            pass

    # Indicate that Data Loading is complete.
    print("-----------------------------")
    print("COVID NOW state data retrieval complete.......")
    print("----")


    covid_state_csv_df = pd.read_csv(stateurlcsv)
    covid_state_clean_df = covid_state_csv_df.drop(['level','lat','locationId','long','metrics.infectionRate','metrics.infectionRateCI90','metrics.icuHeadroomRatio','metrics.icuHeadroomRatio','metrics.icuCapacityRatio','lastUpdatedDate','url','metrics.testPositivityRatioDetails.source','metrics.contactTracerCapacityRatio','metrics.icuHeadroomDetails','actuals.positiveTests','actuals.negativeTests','actuals.contactTracers','actuals.vaccinesDistributed','riskLevels.overall', 'riskLevels.testPositivityRatio','riskLevels.caseDensity','riskLevels.contactTracerCapacityRatio','riskLevels.infectionRate','riskLevels.icuHeadroomRatio','riskLevels.icuCapacityRatio'], axis=1)
    covid_state = covid_state_clean_df.rename({'metrics.testPositivityRatio':'PositivityRatio',
    'metrics.caseDensity':'Density', 
    'actuals.cases':'ActualCases',
    'actuals.deaths':'ActualDeaths',
    'actuals.hospitalBeds.capacity':'ActualHospitalBedCapacity',
    'actuals.hospitalBeds.currentUsageTotal':'ActualHospitalBedCurrentUsageTotal',
    'actuals.hospitalBeds.currentUsageCovid':'ActualHospitalBedCurrentUsageCovid',
    'actuals.hospitalBeds.typicalUsageRate':'ActualHospitalBedTypicalUsageRate',
    'actuals.icuBeds.capacity':'ActualIcuBedsCapacity',
    'actuals.icuBeds.currentUsageTotal':'ActualIcuBedCurrentUsageTotal',
    'actuals.icuBeds.currentUsageCovid':'ActualIcuBedCurrentUsageCovid',
    'actuals.icuBeds.typicalUsageRate':'ActualIcuBedTypicalUsageRate',
    'actuals.newCases':'ActualNewCases',
    'actuals.vaccinationsInitiated':'ActualVaccinationInitiated',
    'actuals.vaccinationsCompleted':'ActualVaccinationCompleted',
    'metrics.vaccinationsInitiatedRatio':'VaccinationInitaitedRatio',
    'metrics.vaccinationsCompletedRatio':'VaccinationCompletedRatio',
    'actuals.newDeaths':'ActualNewDeaths',
    'actuals.vaccinesAdministered':'ActualVaccinesAdministered'
    }, axis=1)
    
    covid_state.to_csv (r'./database_file/covidbystatefromcsv.csv', index = False, header=True)

    # with open(f'./covid_by_state.json', mode='r') as file:
    #     covid_state_raw = json.load(file)

    # covid_state_df = pd.DataFrame(covid_state_raw) 
    # covid_state_clean_df = covid_state_df.drop(['lat','locationId','long','annotations','lastUpdatedDate','url' ], axis=1)
    # covid_state_clean_df.to_csv (r'./database_file/covidbystate.csv', index = False, header=True) 

    state_epa_df = pd.DataFrame(stateepa)
    state_epa_df.to_csv (r'./database_file/epabystate.csv', index = False, header=True) 

    is_import_complete = import_covid_by_state_to_sqlite()

    if is_import_complete:
        print("-----------------------------")
        print("COVID NOW state data import to sqlite is complete......")
        print("----")
    
    # Call to generate linear regression model
    linear_regression_model(stateSelected)
    

    return render(request, "submitted.html",{"stateSelected": stateSelected})
    



def import_covid_by_state_to_sqlite():

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

        # Show covidbystate table
        #cursor.execute('select * from covidbystate;')

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


def linear_regression_model(state):

    model_data = list_model_data_by_state(state)
    print (model_data)
