from django.db import models
from enum import Enum

DEFAULT_REWARD_ID = 1;
class PlayerClassChoise(Enum):
    RG = "Rogue"
    WR = "Warior"
    MG = "Mage"

# Create your models here.
class Player(models.Model):

    def __str__(self):
        return self.playerClass + " lvl " + self.playerLvl
    playerClass = models.CharField(
        max_length=5,
        choices=[(tag,tag.value) for tag in PlayerClassChoise]
    )
    playerLvl = models.IntegerField(default=0)

class Reward(models.Model):

    def __str__(self):
        return "Reward is " + self.size + " gold and " + self.artefacts
    size = models.IntegerField()
    artefacts =  models.CharField(max_length=255,default = "Nothing")     

class Quest(models.Model):

    def __str__(self):
        return "Quest for "+self.preferedClass + " lvl " + self.requiredLvl
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE, default=DEFAULT_REWARD_ID)
    preferedClass =models.CharField (
        max_length=5,
        choices=[(tag,tag.value) for tag in PlayerClassChoise]
    )
    requiredLvl = models.IntegerField(default=0)  
