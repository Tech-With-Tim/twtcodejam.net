from django.urls import path
from . import views


app_name = 'timathon'
urlpatterns = [
    path('', views.home, name="Home"),
    path('createteam', views.create_team, name="Create_Team"),
    path('ViewTeams',views.view_teams, name="ViewTeams")
]

