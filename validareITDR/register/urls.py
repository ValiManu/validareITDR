from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('activate/<uidb64>/<token>', views.activate_account, name='activate'),
    path('username/', views.is_username, name='is_username'),
    path('email/', views.is_email, name='is_email'),
    path('is_password', views.is_password, name='is_password'),
]
