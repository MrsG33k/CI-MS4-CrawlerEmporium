from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_backpack, name='view_backpack'),
    path('add/<item_id>/', views.add_to_backpack, name='add_to_backpack'),
    path('remove/<item_id>/', views.remove_from_backpack, name='remove_from_backpack'),
    path('update/<item_id>/',views.update_backpack, name='update_backpack'),
]
