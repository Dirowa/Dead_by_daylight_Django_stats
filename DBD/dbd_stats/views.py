from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from django.shortcuts import render
from .forms import Game_form_entree
import datetime
from rest_framework.renderers import JSONRenderer

from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Game
from .serializers import GameSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,mixins, generics
from .utils import *


# Include the `fusioncharts.py` file that contains functions to embed the charts.

def index(request):
    return render(request, "dbd_stats/welcome_page.html")


def get_game_data(request):
    initial_data ={"pub_date":datetime.now()}
    if request.method == "POST": #data send by user
        form = Game_form_entree(request.POST,initial=initial_data)        # create a form instance and populate it with data from the request:

        # check whether it's valid:
        if form.is_valid():
            form.save() #safe data to database
            # redirect to a new URL:
            return HttpResponseRedirect("submit_data/thanks")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Game_form_entree()

    context = {"dbd_form": form}
    return render(request, "dbd_stats/form_template.html", context=context)

def thanks(request):

    return  render(request, "dbd_stats/form_succes.html")

#adding

def statistics(request):
    serializer = GameSerializer(Game.objects.all(), many=True)
    data = (serializer.data)
    data = CreateData((data))
    context = {"games_a_day": data.get_plot_histogram()}

    return render(request, "dbd_stats/statistics.html",context=context)


class game_list(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GamesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

