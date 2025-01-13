from django.urls import path
from . import views

urlpatterns = [
    path("", views.showNavBar, name='showNavBar'),
    # path("", views.index, name="index"),
]