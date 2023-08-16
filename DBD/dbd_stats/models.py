from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


killer_choices = (
    ("The Trapper","The Trapper"),
    ("The Hillbilly","The Hillbilly"),
    ("The Hag","The Hag"),
    ("Huntress","Huntress"),
    ("Micheal Myers","Micheal Myers",),
    ("The Plague","The Plague"),
    ("The spirit","The spirit"),
    ("The Oni","The Oni"),
    ("The Legion","The Legion"),
    ("The Artist","The Artist"),
    ("ghost face","ghost face"),
    ("The Cannibal","The Cannibal"),
    ("The pig","The pig"),
    ("The Doctor","The Doctor"),
    ("The Nurse","The Nurse"),
    ("Nemesis","Nemesis"),
    ("Demogorgon", "Demodogo"),
    ("The Trickster","The Trickster"),
    ("The Blight","The Blight"),
    ("The Cenobite","The Cenobite"),
    ("Freddy Krueger","Freddy Krueger"),
    ("The Clown","The Clown"),
    ("The Wraith","The Wraith"),
    ("The Twins","The Twins"),
    ("Pyramid head","Pyramid head"),
    ("DeathSlinger","DeathSlinger"),
    ("The knight","The knight"),
    ("The skull merchant","The skull merchant"),
    ("Dredge","Dredge"),
    ("Mastermind","Mastermind"),
    ("The Onryo","The Onryo"))

map_choices=(
    ("Raccoon City","Raccoon City"),
    ("Midwitch elementary school","Midwitch elementary school"),
    ("Garden of Joy","Garden of joy"),
    ("The MacMillan Estate","The MacMillan Estate"),
    ("Autohaven Wreckers","Autohaven Wreckers"),
    ("Coldwind Farm","Coldwind Farm"),
    ("Crotus Prenn Asylum","Crotus Prenn Asylum"),
    ("Haddonfield","Haddonfield"),
    ("Backwater Swamp","Backwater Swamp"),
    ("Léry's Memorial Institute","Léry's Memorial Institute"),
    ("Red Forest","Red Forest"),
    ("Springwood","Springwood"),
    ("Gideon Meat Plant","Gideon Meat Plant"),
    ("Yamaoka Estate","Yamaoka Estate"),
    ("Ormond","Ormond"),
    ("Grave of Glenvale","Grave of Glenvale"),
    ("Silent Hill","Silent Hill"),
    ("Forsaken Boneyard","Forsaken Boneyard")


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
    Game_map = models.CharField(max_length=26, choices=map_choices, default="Raccoon City")
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

    class Meta:
        ordering = ["pub_date"]

