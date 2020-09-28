from django.urls import path
from . import views


app_name = 'timathon'
urlpatterns = [
    path('', views.home, name="Home"),
    path('newteam/', views.create_team, name="Create_Team"),
    path('team/<int:challenge_id>/', views.view_teams, name="ViewTeams"),
    path('submit/', views.submission, name="Submission")
]
