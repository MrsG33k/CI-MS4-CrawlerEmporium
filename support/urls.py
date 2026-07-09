from django.urls import path
from . import views

urlpatterns = [
    path('', views.crawler_support, name='crawler_support'),
]
