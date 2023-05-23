from django.urls import path

from . import views

app_name = "DBD_tracker"
urlpatterns = [
    path("", views.index, name="index"),
    path("submit_data", views.get_game_data, name="submit_data"),
    path("submit_data/thanks", views.thanks, name="Thanks")
]