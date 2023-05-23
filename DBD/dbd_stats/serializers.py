from rest_framework import serializers
from .models import Game
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class GameSerializer(serializers.ModelSerializer):
     class Meta:
        model = Game
        fields = "__all__"
