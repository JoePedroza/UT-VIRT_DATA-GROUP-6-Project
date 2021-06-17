# UT-VIRT-DATA-Group-6-Project

## Project Background: Particulate Matter and COVID-19 Outcomes

Air pollution is a major public health concern due to its negative impact on individual and population health. A major component of air pollution is particulate matter (PM), which is the solid and liquid particles suspended in air. PM can enter the body through various route depending on the size, shape, and concentration. However, the most common route is inhalation, which negatively affect areas of the respiratory, cardiovascular, cardiopulmonary, and reproductive systems.

![Particulatematter](Resources/ParticulateMatter.PNG)

PM 2.5, for example, can reach the lower respiratory system. Studies have shown that increased concentrations of fine particulate matter can cause elevated susceptibility to respiratory disease. This, in turn, may exascerbate the symptoms caused by COVID-19, and increase hospitalizations and deaths due to COVID-19.

### Project Objective

For our final project, we have chosen to create a machine learning model to assess the relationship between PM2.5 (atmospheric particulate matter with diameter less than 2.5 μm) and the clinical outcomes of COVID-19. The question we hope to answer is as follows: does increased concentrations of particulate matter contribute to an increase in the severity of COVID-19 symptoms, and lead to higher hospitalization and death rates?

We selected this topic (PM 2.5 and COVID-19) becuase this disease has had an immense impact on the world. Understanding what exascerbates COVID-19 symptoms - contributes to COVID associated hospitalizations and death - is an important and fascinating area of study. This is also a great opportunity to exercise the skills we've learned in our data analysis program.

## Database Integration

Pulling data from covidactnow.org and US EPA using following api:

- [covidactnow.org](apidocs.covidactnow.org)
- [United States Evironmental Protection Agency](https://www.epa.gov/air-trends/air-quality-cities-and-counties)

## Database Design

![CovidDatabaseDesign](Resources/CovidProjectDatabaseDesign.png)

## Google Slide Draft

[Google Slide Draft presentation](https://docs.google.com/presentation/d/1QtQoBtW4AktTGot_MRScFSNJ2KotpPKPlfP7MPlIExM/edit#slide=id.p)

## Machine Learning Model

The basic procedure for implementing a supervised learning model is as follows:

- Create a model with LogisticRegression().
- Train the model with model.fit().
- Make predictions with model.predict().
- Validate the model with accuracy_score().

Our model will use logistic regression to predict a binary outcome - two possible outcomes. Our logistic regression will be able to decide, based on county level data, whether higher concentrations of PM 2.5 is associated with increased COVID-19 hospitalizations and deaths.

## Presentation
Here is a link to our google slides presentation
- https://docs.google.com/presentation/d/1QtQoBtW4AktTGot_MRScFSNJ2KotpPKPlfP7MPlIExM/edit?usp=sharing

Also, checkout our dashboard at the following link:
https://ut-covid-project.herokuapp.com/


### Database Design

![](Resources/CovidProjectSqliteDB.png)


### Description of the tool(s) that will be used to create final dashboard

### Python: Getting Started

A barebones Django app, which can easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

### Running Locally

Make sure you have Python 3.9 [installed locally](https://docs.python-guide.org/starting/installation/). To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone https://github.com/heroku/python-getting-started.git
$ cd python-getting-started

$ python3 -m venv getting-started
$ pip install -r requirements.txt

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

### Deploying to Heroku

```sh
$ heroku create
$ git push heroku main

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### Documentation

---go to:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)




### Project Topic: Particulate Matter and COVID-19 Outcomes
Air pollution is a major public health concern due to its negative impact on individual and population health. A major component of air pollution is particulate matter - all the solid and liquid particles suspended in air. Particulate matter (PM) can enter the body through inhalation, and may negatively impact peoples' respiratory, cardiovascular, cardiopulmonary, and reproductive systems. The route of entry - and system affected - depends on the size, shape, and concentration or density of the particulate matter.

We have chosen PM 2.5, specifically, because this size of particulate matter can reach the lower respiratory system. Studies have shown that increased concentrations of fine particulate matter can cause elevated susceptibility to respiratory disease. This, in turn, may exascerbate the symptoms caused by COVID-19, and increase hospitalizations and deaths due to COVID-19.


## Machine Learning Model (see Covid_PM_Model.ipynb for basic script outline)
Present a provisional machine learning model that stands in for the final machine learning model and accomplishes the following:

- Takes in data from the provisional database
- Outputs label for input data

The basic procedure for implementing a supervised learning model is as follows: create a model, train the model, and then create predictions.

Our model will use logistic regression to predict a binary outcome - two possible outcomes. Our logistic regression will be able to decide, based on county level data, whether higher concentrations of PM 2.5 is associated with increased COVID-19 hospitalizations and deaths.

 We'll take the following steps to use a logistic regression model:

- Create a model with LogisticRegression().
- Train the model with model.fit().
- Make predictions with model.predict().
- Validate the model with accuracy_score().

## Database Integration
Pulling data from covidactnow.org and US EPA using following api:
- apidocs.covidactnow.org
- United States Evironmental Protection Agency
- - https://www.epa.gov/air-trends/air-quality-cities-and-counties


### Database Design

![](Resources/CovidProjectDatabaseDesign.PNG)


### Google Slides
https://docs.google.com/presentation/d/1QtQoBtW4AktTGot_MRScFSNJ2KotpPKPlfP7MPlIExM/edit?usp=sharing



## Project objective

build a machine learning model that predicts, base on the size amd concentration of particulate matter inhaled, number of hopitalizations or deaths due to COVID-19 symptoms.

## Table of contents

* [Project Overview](#Project-Overview)
* [Selected topic](#Selected-topic)
* [Reason topic was selected](#Reason-topic-was-selected)
* [Description of the source of data](#Description-of-the-source-of-data)
* [Questions the team hopes to answer with the data](#Questions-the-team-hopes-to-answer-with-the-data)
* [Description of the data exploration phase of the project](#Description-of-the-data-exploration-phase-of-the-project)
* [Description of the analysis phase of the project](#Description-of-the-analysis-phase-of-the-project).
* [Technologies, Languages, tools, and algorithms used throughout the project](#Technologies-Languages-tools-and-algorithms-used-throughout-the-project)


## Description of the project

The project is divided into four parts. The project will show case skills gained through this Boot Camp and be ready to apply them in real life

1. First part:

    - Select a topic for the project (i.e. questions we hope to answer using our datasets()).
    - Create a repository for the project and invite the other team members to join.
    - Source a dataset or datasets that will suit our needs.
    - Clean, organize, and perform exploratory data analysis on our dataset(s) so that they're ready for analysis.
    - Build a simple model and connect to a fake dataset(s).

2. Second part:

    - Continue on the foundation layered out in the first part.
    - Continue on training the model.
    - Build the database for use on the final presentation.

3. Third part:

    - Coonect model to the database.
    - Continue on training the model.
    - Create the dashboard and the presentation.

4. Fourth part:

    - Review the first-three parts and make any changes necessary.
    - Present your project milstones.
