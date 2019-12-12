from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
# <int:type_num>
    path('careerGuide', views.guidecontent),
    path('jobList/', views.jobList),
]
