from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


killer_choices = (
    ("Evan MacMillan","The Trapper"),
    ("Max Thompson Jr","The Hillbilly"),
    ("Lisa Sherwood","The Hag"),
    ("Anna","Huntress"),
    ("Micheal Myers","The Shape"),
    ("Adiris","The Plague"),
    ("Rin Yamaoka","The spirit"),
    ("Kazan Yamaoka","The Oni"),
    ("Frank","The Legion"),
    ("Carmina Mora","The Artist"),
    ("Danny Johnson","ghost face"),
    ("Bubba Sawyer","The Cannibal"),
    ("Amanda Sawyer","The pig"),
    ("Herman Carter","The Doctor"),
    ("Sally Smithson","The Nurse"),
    ("Nemesis","Nemesis"),
    ("Demogorgon", "Demodogo"),
    ("Ji-woon Hak","The Trickster"),
    ("Talbot Grimes","The Blight"),
    ("Elliot Spencer / pinhead","The Cenobite"),
    ("Freddy Krueger","Nightmare"),
    ("Jeffrey Hawk","The Clown"),
    ("Phillip Ojomo","The Wraith"),
    ("Victor & Charlotte","The Twins"),
    ("Pyramid head","Executioner"),
    ("Caleb Quin","DeathSlinger"),
    ("Tarhos Kovacs","The knight"),
    ("Adrianaimai","The skull merchant"),
    ("Dredge","Dredge"),
    ("Albert Wesker","Mastermind"),
    ("Sadoko Yamamura","The Onryo"))

map_choices=(
    ("Raccoon City","Raccoon City"),
    ("Silent Hill","Midwitch elementary school"),
    ("Garden of Joy","Garden of joy")
)

faul_play_Choices = (
    ("face camping","face camping"),
    ("Tunneling","Tunneling"),
    ("NA","NA"),
    ("camping","camping")
)
mood_players = (("FUN","FUN"),
             ("Irritated","rritated"),
             ("tired","tired"),
             ('meh',"meh"),
             )

play_style_choices = (("normal", "normal"),
                      ("meme","meme"),
                      ("Sweat","sweat"),
                      ("Challanges","challanges"))
class Game(models.Model):

    pub_date = models.DateTimeField("date published")
    killer = models.CharField(max_length=24, choices=killer_choices,default="The Trapper")
    mori = models.BooleanField(default=False)
    Insta_down = models.BooleanField(default=False)
    sweat = models.IntegerField(default=5,validators=[MinValueValidator(0),MaxValueValidator(10)])
    Game_map = models.CharField(max_length=24, choices=map_choices, default="Raccoon City")
    deaths =  models.IntegerField(default=4,validators=[MinValueValidator(0),MaxValueValidator(4)])
    Gens_completed =  models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(5)])
    Faul_play = models.CharField(max_length=20, choices=faul_play_Choices, default="NA")
    overal_fun = models.IntegerField(default=5,validators=[MinValueValidator(0),MaxValueValidator(10)])
    player_1 = models.CharField(max_length=9, choices=mood_players,default="FUN")
    player_2 = models.CharField(max_length=9, choices=mood_players,default="FUN")
    player_3 = models.CharField(max_length=9, choices=mood_players,default="FUN")
    player_4 = models.CharField(max_length=9, choices=mood_players,default="FUN")
    overall_play_style = models.CharField(max_length=10, choices=play_style_choices,default="normal")


    def __str__(self):
        return f"{self.killer}_{self.pub_date}"

    def max_death(self):
        return self.deaths <= 4

    def max_gens(self):
        return self.Gens_completed <= 5

