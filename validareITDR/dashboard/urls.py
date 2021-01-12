from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('change-campaign/', views.change_campaign, name='campaign'),
    path('set-campaign/', views.set_campaigns, name='set_campaign'),
    path('test/', views.dashboard_report, name='dashboard')
]
