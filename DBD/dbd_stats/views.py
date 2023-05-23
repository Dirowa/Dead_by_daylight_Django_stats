from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
import time
from django.shortcuts import render
from .forms import Game_form_entree
import datetime

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Game
from .serializers import GameSerializer

def index(request):
    return render(request, "dbd_stats/welcome_page.html")


def get_game_data(request):
    initial_data ={"pub_date":datetime.datetime.now()}
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
    return render(request, "dbd_stats/statistics.html")

@csrf_exempt
def game_list(request):
    if request.method == "GET":
        game = Game.object.all()
        serializer = GameSerializer(game,many=True)
        return(JsonResponse(serializer.data,safe=False))

    elif request.method == "POST":
        data =JSONParser().parse(request)
        serializer = GameSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors, status=400)

def game_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = GameSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = GameSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        Game.delete()
        return HttpResponse(status=204)