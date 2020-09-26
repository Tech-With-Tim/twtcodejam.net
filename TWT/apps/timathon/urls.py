from django.urls import path
from . import views


app_name = 'timathon'
urlpatterns = [
    path('', views.home, name="Home")
]
