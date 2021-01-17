from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('change-campaign/', views.change_campaign, name='campaign'),
    path('set-campaign/', views.set_campaigns, name='set_campaign'),
    path('sales/report', views.sales_report, name='sales_report'),
    path('prize/report', views.prize_list_report, name='prize_report')
]
