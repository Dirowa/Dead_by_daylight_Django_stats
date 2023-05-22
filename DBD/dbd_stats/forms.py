
from .models import Game
import datetime
from django.forms import ModelForm, Textarea
class Game_form_entree(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['pub_date'].initial = datetime.datetime.now()
    class Meta:
        model = Game
        fields = "__all__"

