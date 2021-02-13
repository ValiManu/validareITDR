from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('change-campaign/', views.change_campaign, name='campaign'),
    path('set-campaign/', views.set_campaigns, name='set_campaign'),
    path('sales/report', views.sales_report, name='sales_report'),
    path('prize/report', views.prize_list_report, name='prize_report'),
    path('campaigns-display/', views.campaigns_display, name='campaigns_display'),
    path('add-campaign/', views.add_campaign, name='add_campaign'),
    path('edit-campaign/<int:pk>', views.edit_campaign, name='edit_campaign'),
    path('is-campaign-name', views.is_campaign_name, name='is_campaign_name'),

]
