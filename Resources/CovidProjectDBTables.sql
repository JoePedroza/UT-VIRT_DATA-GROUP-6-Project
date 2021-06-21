-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "COVIDCases" (
    "FipCode" int   NOT NULL,
    "Country" varchar   NOT NULL,
    "State" varchar   NOT NULL,
    "County" varchar   NOT NULL,
    "Level" varchar   NOT NULL,
    "Population" int   NOT NULL,
    "PositivityRatio" decimal   NOT NULL,
    "PositivityRatioSource" varchar   NOT NULL,
    "Density" int   NOT NULL,
    "InfectionRatio" decimal   NOT NULL,
    "InfectionRatioCI90" decimal   NOT NULL,
    "IcuHeadRoomRatio" decimal   NOT NULL,
    "IcuCapacityRatio" decimal   NOT NULL,
    "RiskLevelOverall" int   NOT NULL,
    "RiskLevelPositivityRatio" decimal   NOT NULL,
    "RiskLevelCaseDensity" int   NOT NULL,
    "RiskLevelContactTracerCapacityRatio" decimal   NOT NULL,
    "RiskLevelInfectionRate" decimal   NOT NULL,
    "RiskLevelICUHeadRoomRatio" decimal   NOT NULL,
    "RiskLevelsICUCapacityRatio" decimal   NOT NULL,
    "ActualCases" int   NOT NULL,
    "ActualDeaths" int   NOT NULL,
    "ActualHospitalBedCapacity" int   NOT NULL,
    "ActualHospitalBedCurrentUsageTotal" int   NOT NULL,
    "ActualHospitalBedCurrentUsageCovid" int   NOT NULL,
    "ActualHospitalBedTypicalUsageRate" decimal   NOT NULL,
    "ActualIcuBedsCapacity" int   NOT NULL,
    "ActualIcuBedCurrentUsageTotal" int   NOT NULL,
    "ActualIcuBedCurrentUsageCovid" int   NOT NULL,
    "ActualIcuBedTypicalUsageRate" decimal   NOT NULL,
    "ActualNewCases" int   NOT NULL,
    "ActualVaccinationInitiated" int   NOT NULL,
    "ActualVaccinationCompleted" int   NOT NULL,
    "VaccinationInitaitedRatio" decimal   NOT NULL,
    "VaccinationCompletedRatio" decimal   NOT NULL,
    "ActualNewDeaths" int   NOT NULL,
    "ActualVaccinesAdministered" int   NOT NULL
);

CREATE TABLE "COVIDCasesTimeSeries" (
    "Date" date   NOT NULL,
    "Country" varchar   NOT NULL,
    "State" varchar   NOT NULL,
    "County" varchar   NOT NULL,
    "FipCode" int   NOT NULL,
    "Level" varchar   NOT NULL,
    "Population" int   NOT NULL,
    "PositivityRatio" decimal   NOT NULL,
    "PositivityRatioSource" varchar   NOT NULL,
    "Density" decimal   NOT NULL,
    "InfectionRatio" decimal   NOT NULL,
    "InfectionRatioCI90" decimal   NOT NULL,
    "IcuHeadRoomRatio" decimal   NOT NULL,
    "IcuCapacityRatio" decimal   NOT NULL,
    "RiskLevelOverall" int   NOT NULL,
    "RiskLevelPositivityRatio" decimal   NOT NULL,
    "RiskLevelCaseDensity" decimal   NOT NULL,
    "RiskLevelContactTracerCapacityRatio" decimal   NOT NULL,
    "RiskLevelInfectionRate" decimal   NOT NULL,
    "RiskLevelICUHeadRoomRatio" decimal   NOT NULL,
    "RiskLevelsICUCapacityRatio" decimal   NOT NULL,
    "ActualCases" int   NOT NULL,
    "ActualDeaths" int   NOT NULL,
    "ActualHospitalBedCapacity" int   NOT NULL,
    "ActualHospitalBedCurrentUsageTotal" int   NOT NULL,
    "ActualHospitalBedCurrentUsageCovid" int   NOT NULL,
    "ActualHospitalBedTypicalUsageRate" decimal   NOT NULL,
    "ActualIcuBedsCapacity" int   NOT NULL,
    "ActualIcuBedCurrentUsageTotal" int   NOT NULL,
    "ActualIcuBedCurrentUsageCovid" int   NOT NULL,
    "ActualIcuBedTypicalUsageRate" decimal   NOT NULL,
    "ActualNewCases" int   NOT NULL,
    "ActualVaccinationInitiated" int   NOT NULL,
    "ActualVaccinationCompleted" int   NOT NULL,
    "VaccinationInitaitedRatio" decimal   NOT NULL,
    "VaccinationCompletedRatio" decimal   NOT NULL,
    "ActualNewDeaths" int   NOT NULL,
    "ActualVaccinesAdministered" int   NOT NULL
);

CREATE TABLE "AirQualityByCounty" (
    "State" varchar   NOT NULL,
    "County" varchar   NOT NULL,
    "FipCode" int   NOT NULL,
    "Population" int   NOT NULL,
    "CO8hr" int   NOT NULL,
    "Pb3Mo" decimal   NOT NULL,
    "NO2" int   NOT NULL,
    "AMPpb" int   NOT NULL,
    "NO2Hr" int   NOT NULL,
    "038Hr" decimal   NOT NULL,
    "PM10_24Hr" int   NOT NULL,
    "PM25_Wtd_AM" decimal   NOT NULL,
    "PM25_24Hr" int   NOT NULL,
    "SO2_1Hr" int   NOT NULL
);

CREATE TABLE "FIPS" (
    "FipCode" int   NOT NULL,
    "Name" varchar   NOT NULL,
    "State" varchar   NOT NULL,
    CONSTRAINT "pk_FIPS" PRIMARY KEY (
        "FipCode"
     )
);

ALTER TABLE "COVIDCases" ADD CONSTRAINT "fk_COVIDCases_FipCode" FOREIGN KEY("FipCode")
REFERENCES "FIPS" ("FipCode");

ALTER TABLE "COVIDCasesTimeSeries" ADD CONSTRAINT "fk_COVIDCasesTimeSeries_FipCode" FOREIGN KEY("FipCode")
REFERENCES "FIPS" ("FipCode");

ALTER TABLE "AirQualityByCounty" ADD CONSTRAINT "fk_AirQualityByCounty_FipCode" FOREIGN KEY("FipCode")
REFERENCES "FIPS" ("FipCode");

