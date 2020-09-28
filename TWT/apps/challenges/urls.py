from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home',),
    path('logout/', views.logout, name="logout"),
    path('new/', views.new, name="new"),
    path('view/<int:challenge_id>/', views.view, name="view"),
    path('start/<int:challenge_id>/', views.start, name="start"),
    path('end/<int:challenge_id>/', views.end, name="end"),
    path('startsubmission/<int:challenge_id>', views.start_submission, name="StartSubmission"),
    path('stopsubmission/<int:challenge_id>', views.stop_submission, name="StopSubmissions"),
    path('stopteams/<int:challenge_id>', views.stop_team, name="StopTeams")
]
