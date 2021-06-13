# UT-VIRT-DATA-Group-6-Project

### Segment Overview
In segment one we'll complete the following tasks:
- Create the foundation for the final project and - importantly - decide on a topic/question that can be answered using data
- Define roles between team members and establish a team communication structure
- Source a dataset, and begin to clean, organize, and perform exploratory data analysis
- Create mockups of a machine learning model, a database, and a firm grasp of how you want these different pieces to interact

### Project Topic: Particulate Matter and COVID-19 Outcomes
Air pollution is a major public health concern due to its negative impact on individual and population health. A major component of air pollution is particulate matter - all the solid and liquid particles suspended in air. Particulate matter (PM) can enter the body through inhalation, and may negatively impact peoples' respiratory, cardiovascular, cardiopulmonary, and reproductive systems. The route of entry - and system affected - depends on the size, shape, and concentration or density of the particulate matter.

![](Resources/ParticulateMatter.jpg)

We have chosen PM 2.5, specifically, because this size of particulate matter can reach the lower respiratory system. Studies have shown that increased concentrations of fine particulate matter can cause elevated susceptibility to respiratory disease. This, in turn, may exascerbate the symptoms caused by COVID-19, and increase hospitalizations and deaths due to COVID-19.



## Python: Getting Started

A barebones Django app, which can easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Running Locally

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

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku main

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentation

---go to:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
