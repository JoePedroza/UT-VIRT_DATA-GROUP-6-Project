import sqlite3
import hashlib
import datetime

user_db_file_location = "database_file/users.db"
note_db_file_location = "database_file/notes.db"
image_db_file_location = "database_file/images.db"
county_db_file_location = "database_file/counties.db"

def list_counties(state):
    _conn = sqlite3.connect(county_db_file_location)
    _c = _conn.cursor()

    _c.execute("SELECT name, fipscode FROM counties WHERE state = '" + state + "';")
    result = [x[0] for x in _c.fetchall()]

    _conn.close()
    
    return result

def list_states():
    _conn = sqlite3.connect(county_db_file_location)
    _c = _conn.cursor()

    _c.execute("SELECT abbr FROM states;")
    result = [x[0] for x in _c.fetchall()]

    _conn.close()
    
    return result

def list_epa_by_state(state):
    _conn = sqlite3.connect(county_db_file_location)
    _c = _conn.cursor()

    _c.execute("SELECT e.state, e.county, e.fipcode, e.population, e.CO_8hr, e.PB_3mo,e.NO2_AM, e.NO2_1hr, e.O3_8hr, e.PM10_24hr, e.PM25_Wtd_AM, e.PM25_24hr, e.SO2_1hr  FROM states s INNER JOIN epa e ON s.name = e.state INNER JOIN counties c ON e.fipcode = c.fipscode WHERE  c.state ='" + state + "';")
    result = _c.fetchall()

    _conn.close()
    
    return result    


def list_model_data_by_state(state):
    _conn = sqlite3.connect(county_db_file_location)
    _c = _conn.cursor()

    _c.execute("SELECT e.state, e.county, e.fipcode, e.population, PositivityRatio,Density,ActualCases,ActualDeaths,ActualHospitalBedCapacity,ActualHospitalBedCurrentUsageTotal,ActualHospitalBedCurrentUsageCovid,ActualHospitalBedTypicalUsageRate,ActualIcuBedsCapacity,ActualIcuBedCurrentUsageTotal,ActualIcuBedCurrentUsageCovid,ActualIcuBedTypicalUsageRate,ActualNewCases,ActualVaccinationInitiated,ActualVaccinationCompleted,VaccinationInitaitedRatio,VaccinationCompletedRatio,ActualNewDeaths,ActualVaccinesAdministered, e.CO_8hr, e.PB_3mo,e.NO2_AM, e.NO2_1hr, e.O3_8hr, e.PM10_24hr, e.PM25_Wtd_AM, e.PM25_24hr, e.SO2_1hr  FROM states s INNER JOIN epa e ON s.name = e.state INNER JOIN counties c ON e.fipcode = c.fipscode  INNER JOIN covidbystate cov ON cov.fips = c.fipscode WHERE  c.state ='" + state + "';")
    result = _c.fetchall()

    _conn.close()
    
    return result        


if __name__ == "__main__":
    print(list_states())
