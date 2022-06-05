from django.urls import path, include
from . import views

appName = 'smalltown'

urlpatterns = [
    path('', views.home, name='homee'),
]