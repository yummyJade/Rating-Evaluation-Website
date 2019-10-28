from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
# <int:type_num>
    path('naire/', views.infoform),
    path('getNaire/', views.getNaire),
    path('calcuNaire/', views.calcuNaire),
    path('', views.hello),
]
