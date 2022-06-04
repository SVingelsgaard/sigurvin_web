from django.urls import path, include
from . import views

appName = 'homepage'

urlpatterns = [
    path('', views.home, name='home'),
]