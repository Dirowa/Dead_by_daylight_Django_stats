from django.urls import path

from . import views
from .views import get_game_data

urlpatterns = [
    path("", views.index, name="index"),
    path("add_dbd_data",get_game_data, name="submit_form"),
]