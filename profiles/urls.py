from django.urls import path
from . import views

urlpatterns = [
    path('vault/', views.profile_vault, name='profile_vault'),
    path('settings/', views.account_settings, name='account_settings'),
]