from rest_framework import serializers
from .models import Game
from django.core.validators import MaxValueValidator, MinValueValidator

class GameSerializer(serializers.ModelSerializer):
     class Meta:
        model = Game
        fields = "__all__"

#    def create(self, validated_data):
#        return Game.objects.create(**validated_data)

 #   def update(self, instance, validated_data):
 #       instance.pub_date = validated_data.get('pub_date',instance.pub_date)
 #       instance.killer = validated_data.get('killer',instance.killer)
 #       instance.Insta_down = validated_data.get('Insta_down',instance.Insta_down)
 #       instance.sweat = validated_data.get('sweat',instance.sweat)
 #       instance.Game_map = validated_data.get('Game_map',instance.Game_map)
 #       instance.deaths = validated_data.get('deaths',instance.deaths)
 #       instance.Gens_completed = validated_data.get('Gens_completed',instance.Gens_completed)
 #       instance.Faul_play = validated_data.get('Faul_play',instance.Faul_play)
 #       instance.overal_fun = validated_data.get('overal_fun',instance.overal_fun)
 #       instance.player_1 = validated_data.get('player_1',instance.player_1)
 ##       instance.player_2 = validated_data.get('player_2',instance.player_2)
  #      instance.player_3 = validated_data.get('player_3',instance.player_3)
  #      instance.player_4 = validated_data.get('player_4',instance.player_4)
  #      instance.overall_play_style = validated_data.get('overall_play_style',instance.overall_play_style)
  #      instance.save()
  #      return instance

