# UT-VIRT-DATA-Group-6-Project

### Segment 2 Overview:
- Presentation
- Github
- Machine learning model
- Database
- Dashboard 

## Presentation
Here is a link to our google slides presentation
- https://docs.google.com/presentation/d/1QtQoBtW4AktTGot_MRScFSNJ2KotpPKPlfP7MPlIExM/edit?usp=sharing

The presentation outlines the project, and includes the following:
- Selected topic
- Reason why they selected their topic
- Description of their source of data
- Questions they hope to answer with the data
- Description of the data exploration phase of the project
- Description of the analysis phase of the project
- Includes Dashboard storyboard

## Github


## Machine learning model
Team members submit the code for their machine learning model, as well as the following:
- Description of preliminary data preprocessing
- Description of preliminary feature engineering and preliminary feature selection, including their decision-making process
- Description of how data was split into training and testing sets
- Explanation of model choice, including limitations and benefits

The basic procedure for implementing a supervised learning model is as follows: create a model, train the model, and then create predictions.

Our model will use logistic regression to predict a binary outcome - two possible outcomes. Our logistic regression will be able to decide, based on county level data, whether higher concentrations of PM 2.5 is associated with increased COVID-19 hospitalizations and deaths.

 We'll take the following steps to use a logistic regression model:

- Create a model with LogisticRegression().
- Train the model with model.fit().
- Make predictions with model.predict().
- Validate the model with accuracy_score().

## Database
Team members present a fully integrated database.
- Database stores static data for use during the project
- Database interfaces with the project in some format (e.g., scraping updates the database, or database connects to the model)
- Includes at least two tables (or collections, if using MongoDB)
- Includes at least one join using the database language (not including any joins in Pandas)
- Includes at least one connection string (using SQLAlchemy or PyMongo)
Note: If you use a SQL database, you must provide your ERD with relationships.

Pulling data from covidactnow.org and US EPA using following api:
- apidocs.covidactnow.org
- United States Evironmental Protection Agency
- https://www.epa.gov/air-trends/air-quality-cities-and-counties


### Database Design

![](Resources/CovidProjectSqliteDB.png)

## Dashboard

- Storyboard on Google Slide(s)
- Description of the tool(s) that will be used to create final dashboard
- Description of interactive element(s)

- Checkout our dashboard at the following link:
https://ut-covid-project.herokuapp.com/

### Description of the tool(s) that will be used to create final dashboard.



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

------------------------------------------------------------------------------
# Segment One
In segment one we'll complete the following tasks:
- Create the foundation for the final project and - importantly - decide on a topic/question that can be answered using data
- Define roles between team members and establish a team communication structure
- Source a dataset, and begin to clean, organize, and perform exploratory data analysis
- Create mockups of a machine learning model, a database, and a firm grasp of how you want these different pieces to interact

### Project Topic: Particulate Matter and COVID-19 Outcomes
Air pollution is a major public health concern due to its negative impact on individual and population health. A major component of air pollution is particulate matter - all the solid and liquid particles suspended in air. Particulate matter (PM) can enter the body through inhalation, and may negatively impact peoples' respiratory, cardiovascular, cardiopulmonary, and reproductive systems. The route of entry - and system affected - depends on the size, shape, and concentration or density of the particulate matter.

![Particulatematter](Resources/ParticulateMatter.PNG)

We have chosen PM 2.5, specifically, because this size of particulate matter can reach the lower respiratory system. Studies have shown that increased concentrations of fine particulate matter can cause elevated susceptibility to respiratory disease. This, in turn, may exascerbate the symptoms caused by COVID-19, and increase hospitalizations and deaths due to COVID-19.

## Work as a Team
As a virtual team, we share the same goal - but we have different obligations and responsibilities outside of this project. In order to reach our goal, we will communicate through Slack and work concurrently via Github. Group members are expected to meet on Monday and Wednesday nights, communicate regularly, do their best to acheive goals, and reach out if issues arise.

T help our team reach our goal for this segment of the project, we've assigned roles which are outlined below:
- Square: The team member in the square role will be responsible for the repository. (Ibrahim)

- Triangle: The member in the triangle role will create a mockup of a machine learning model. This can even be a diagram that explains how it will work concurrently with the rest of the project steps. (Robert)

- Circle: The member in the circle role will create a mockup of a database with a set of sample data, or even fabricated data. This will ensure the database will work seamlessly with the rest of the project. (Joe)

- X: The member in the X role will decide which technologies will be used for each step of the project. (Edgar)

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

### Dashboard
https://docs.google.com/presentation/d/1QtQoBtW4AktTGot_MRScFSNJ2KotpPKPlfP7MPlIExM/edit?usp=sharing


## Python: Getting Started

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

## Project Topic: Particulate Matter and COVID-19 Outcomes

### Overview of the project

1. Presentation
   We'll prepare a Google slides where we touch bases on the following:
   - Selected topic
   - Reason topic was selected
   - Description of the source of data
   - Questions the team hopes to answer with the data
   - Description of the data exploration phase of the project
   - Description of the analysis phase of the project
   - Technologies, languages, tools, and algorithms used throughout the project

GitHub
Machine learning model
Database
Dashboard

Air pollution is a major public health concern due to its negative impact on individual and population health. A major component of air pollution is particulate matter (PM), which is the solid and liquid particles suspended in air. PM can enter the body through various route depending on the size, shape, and concentration. However, the most common route is inhalation, which negatively affect areas of the respiratory, cardiovascular, cardiopulmonary, and reproductive systems.

![ParticulateMatter](Resources/ParticulateMatter.jpg)

PM 2.5, for example, can reach the lower respiratory system. Studies have shown that increased concentrations of fine particulate matter can cause elevated susceptibility to respiratory disease. This, in turn, may exascerbate the symptoms caused by COVID-19, and increase hospitalizations and deaths due to COVID-19.

### Project Objective: The Question We Hope to Answer

For our final project, we have chosen to create a machine learning model to assess the relationship between PM2.5 (atmospheric particulate matter with diameter less than 2.5 μm) and the clinical outcomes of COVID-19. The question we hope to answer is as follows: does increased concentrations of particulate matter contribute to an increase in the severity of COVID-19 symptoms, and lead to higher hospitalization and death rates?

### Why We Selected This Topic

We selected this topic (PM 2.5 and COVID-19) becuase this disease has had an immense impact on the world. Understanding what exascerbates COVID-19 symptoms - contributes to COVID associated hospitalizations and death - is an important and fascinating area of study. This is also a great opportunity to exercise the skills we've learned in our data analysis program.

## Machine Learning Model(see Covid_PM_Model.ipynb for basic script outline)

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

- [covidactnow.org](apidocs.covidactnow.org)
- [United States Evironmental Protection Agency](https://www.epa.gov/air-trends/air-quality-cities-and-counties)

## Database Design

![CovidDatabaseDesign](Resources/CovidProjectDatabaseDesign.png)

## Google Slide Draft

[Google Slide Draft presentation](https://docs.google.com/presentation/d/1QtQoBtW4AktTGot_MRScFSNJ2KotpPKPlfP7MPlIExM/edit#slide=id.p)