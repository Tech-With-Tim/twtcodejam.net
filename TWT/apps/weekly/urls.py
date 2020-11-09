from django.urls import path
from . import views

app_name = 'weekly'
urlpatterns = [
    path('', views.home, name='home'),
]
