from django.urls import path, include
from . import views

appName = "smalltown"

urlpatterns = [
    path("", views.home, name="home"),
    path("add_grocery", views.add_grocery, name="add_grocery"),
    path("remove_grocery", views.remove_grocery, name="remove_grocery"),
]