from django.urls import path

from django.contrib import admin

admin.autodiscover()

import covid.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", covid.views.index, name="index"),
    path("dashboard/", covid.views.dashboard, name="dashboard"),
    path("getdata/", covid.views.getdata, name="getdata"), 
    path("runmodel/<stateSelected>/", covid.views.runmodel, name="runmodel")
]
