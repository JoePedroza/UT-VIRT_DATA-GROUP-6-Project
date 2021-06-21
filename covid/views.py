# Import Dependencies
from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd
import csv
import sqlite3
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')
from collections import Counter
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import SMOTE
from imblearn.combine import SMOTEENN
from imblearn.under_sampling import ClusterCentroids
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import sklearn.preprocessing as preprocessing
import json
from json import JSONEncoder
from flask import render_template_string


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
    dataRetrieved= False
    modelRan= False
    return render(request, "index.html", {"states" : states})

def dashboard(request):    
    return render(request, "dashboard.html")

def getdata(request): 
    stateSelected= request.POST.get('stateDropdown')
    modelTypes= ['Cluster Centroids','Linear Regression','Logistic Regression','Naive Random Oversampling','Random Undersampling','SMOTE Oversampling','SMOTEENN']
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
    covid_state_clean_df = covid_state_csv_df.replace(np.nan,0)
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

    covid_state.replace({"ND": 0, "IN": 0}, inplace=True)   
    covid_state.to_csv (r'./database_file/covidbystatefromcsv.csv', index = False, header=True)

    state_epa_df = pd.DataFrame(stateepa)
    state_epa_df.to_csv (r'./database_file/epabystate.csv', index = False, header=True) 

    is_import_complete = import_covid_by_state_to_sqlite()

    if is_import_complete:
        print("-----------------------------")
        print("COVID NOW state data import to sqlite is complete......")
        print("----")

    stateData = covid_state
    dataRetrieved= True


    return render(request, "index.html",{"stateSelected": stateSelected,"stateData": stateData, "dataRetrieved": dataRetrieved, "modelTypes": modelTypes})
        

def import_covid_by_state_to_sqlite():

    try:
  
        # Import csv and extract data
        df = pd.read_csv('./database_file/covidbystatefromcsv.csv')

        # Import csv and extract data
        with open('./database_file/covidbystatefromcsv.csv', 'r') as fin:
                dr = csv.DictReader(fin)
                covidbystate_info = [(i['fips'],i['country'], i['state'], i['county'], i['population'], i['PositivityRatio'], i['Density'], i['ActualCases'], i['ActualDeaths'], i['ActualHospitalBedCapacity'],i['ActualHospitalBedCurrentUsageTotal'], i['ActualHospitalBedCurrentUsageCovid'],i['ActualHospitalBedTypicalUsageRate'],i['ActualIcuBedsCapacity'],i['ActualIcuBedCurrentUsageTotal'],i['ActualIcuBedCurrentUsageCovid'],i['ActualIcuBedTypicalUsageRate'],i['ActualNewCases'],i['ActualVaccinationInitiated'],i['ActualVaccinationCompleted'],i['VaccinationInitaitedRatio'],i['VaccinationCompletedRatio'],i['ActualNewDeaths'],i['ActualVaccinesAdministered']) for i in dr]

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


def runmodel(request,stateSelected):

    modelSelected= request.POST.get('modelDropdown')
    model_data = list_model_data_by_state(stateSelected)
    covid_model_df = pd.DataFrame(model_data)
    covid_model_df.to_csv (r'./database_file/covidmodeldata.csv', index = False, header=True) 

    # Load the data
    file_path = Path('database_file/covidmodeldata.csv')
    df = pd.read_csv(file_path)
    covid_df = df.replace(np.nan,0)

    #y = df["ActualHospitalBedCurrentUsageTotal"]
    y = covid_df['9']
    #X = df.drop(['state','county','fipcode','population','ActualHospitalBedCurrentUsageTotal'],axis=1)
    X = covid_df.drop([df.columns[0],df.columns[1],df.columns[2],df.columns[3],df.columns[9]],axis=1)

    #### min-max scaler
    minmax = preprocessing.MinMaxScaler()
    minmax.fit(X)
    X_minmax = minmax.transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_minmax, y, random_state=1)
    X_train.shape

    if modelSelected == 'Linear Regression':
        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        results = pd.DataFrame({"Prediction": y_pred,"Actual": y_test}).reset_index(drop=True)   
    elif modelSelected == 'Logistic Regression':
        model = LogisticRegression(solver='lbfgs', random_state=1)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        results = pd.DataFrame({"Prediction": y_pred,"Actual": y_test}).reset_index(drop=True)
    elif modelSelected == 'Cluster Centroids':
        cc = ClusterCentroids(random_state=1)
        X_resampled, y_resampled = cc.fit_resample(X_train, y_train)
        model = LogisticRegression(solver='lbfgs', random_state=78)
        model.fit(X_resampled, y_resampled)
        y_pred = model.predict(X_test)
        results = pd.DataFrame({"Prediction": y_pred,"Actual": y_test}).reset_index(drop=True)
    elif modelSelected == 'Naive Random Oversampling':
        ros = RandomOverSampler(random_state=1)
        X_resampled, y_resampled = ros.fit_resample(X_train, y_train)
        model = LogisticRegression(solver='lbfgs', random_state=1)
        model.fit(X_resampled, y_resampled)
        y_pred = model.predict(X_test)
        results = pd.DataFrame({"Prediction": y_pred,"Actual": y_test}).reset_index(drop=True)
    elif modelSelected == 'Random Undersampling':
        ros = RandomUnderSampler(random_state=1)
        X_resampled, y_resampled = ros.fit_resample(X_train, y_train)
        model = LogisticRegression(solver='lbfgs', random_state=1)
        model.fit(X_resampled, y_resampled)
        y_pred = model.predict(X_test)
        results = pd.DataFrame({"Prediction": y_pred,"Actual": y_test}).reset_index(drop=True)    
    elif modelSelected == 'SMOTE Oversampling':
        model = SMOTE(random_state=1)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        results = pd.DataFrame({"Prediction": y_pred,"Actual": y_test}).reset_index(drop=True)
    elif modelSelected == 'SMOTEENN':
        smote_enn = SMOTEENN(random_state=0)
        X_resampled, y_resampled = smote_enn.fit_resample(X, y)
        model = LogisticRegression(solver='lbfgs', random_state=1)
        model.fit(X_resampled, y_resampled)
        y_pred = model.predict(X_test)
        results = pd.DataFrame({"Prediction": y_pred,"Actual": y_test}).reset_index(drop=True)
    else:    
        print("No model selected")
        

    model_accuracy_score = accuracy_score(y_test, y_pred)

    model_confusion_matrix =confusion_matrix(y_test, y_pred)

    # Encode NumPy type correctly into JSOn
    encodedNumpyData = json.dumps(model_confusion_matrix, cls=NumpyArrayEncoder)

    model_classification_report = classification_report(y_test, y_pred)

    modelObject = [{
        "Name":"Prediction",
        "Value": results.Prediction,     
    },
    {
        "Name":"Actuals",
        "Value": results.Actual,     
    },
    {
        "Name":"Accuracy Score",
        "Value": model_accuracy_score,     
    },
    {
        "Name":"Confusion Matrix",
        "Value": encodedNumpyData,     
    },
    {
        "Name":"Classification Report",
        "Value": json.dumps(model_classification_report), 
    }
    ]

    modelRan= True
    return render(request, "runmodel.html",{"modelObject": modelObject})



class NumpyArrayEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NumpyArrayEncoder, self).default(obj)



