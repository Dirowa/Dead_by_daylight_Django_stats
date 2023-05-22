from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from .models import Game
from django.shortcuts import render
from .forms import Game_form_entree
import datetime
def index(request):

    latest_question_list = Game.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "dbd_stats/index.html", context)


def get_game_data(request):
    initial_data ={"pub_date":datetime.datetime.now()}
    if request.method == "POST": #data send by user
        form = Game_form_entree(request.POST,initial=initial_data)        # create a form instance and populate it with data from the request:

        # check whether it's valid:
        if form.is_valid():
            form.save() #safe data to database
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Game_form_entree()

    context = {"dbd_form": form}
    return render(request, "dbd_stats/form_template.html", context=context)