from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = "DBD_tracker"
urlpatterns = [
    path("", views.index, name="index"),
    path("submit_data", views.get_game_data, name="submit_data"),
    path("submit_data/thanks", views.thanks, name="Thanks"),
    path("stats", views.statistics, name="stats"),
    path("api",views.game_list),
    path("api/<int:pk>/", views.game_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
