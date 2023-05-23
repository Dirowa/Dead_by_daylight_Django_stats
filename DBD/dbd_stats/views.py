from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from django.shortcuts import render
from .forms import Game_form_entree
import datetime

from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Game
from .serializers import GameSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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

class game_list(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Game.objects.all()
        serializer = GameSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GamesDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        game = self.get_object(pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        game = self.get_object(pk)
        serializer = GameSerializer(game, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        game = self.get_object(pk)
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)