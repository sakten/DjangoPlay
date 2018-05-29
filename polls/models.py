from django.db import models
from enum import Enum

DEFAULT_REWARD_ID = 1

class PlayerClassChoise(Enum):
    def __str__(self):
        return str(self.value)
    Rogue = "Rogue"
    Warior = "Warior"
    Mage = "Mage"

# Create your models here.
class Player(models.Model):

    def __str__(self):
        return  self.playerClass + " lvl " + str(self.playerLvl)

    playerClass = models.CharField(
        max_length=10,
        choices=[(tag, tag.value) for tag in PlayerClassChoise]
    )
    playerLvl = models.IntegerField(default=0)

class Reward(models.Model):

    def __str__(self):
        return "Reward is " + str(self.size) + " gold and " + self.artefacts
    size = models.IntegerField()
    artefacts =  models.CharField(max_length=255,default = "Nothing")     

class Quest(models.Model):

    def __str__(self):
        return "Quest for "+self.preferedClass + " lvl " + str(self.requiredLvl)
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE, default=DEFAULT_REWARD_ID)
    preferedClass =models.CharField (
        max_length=5,
        choices=[(tag,tag.value) for tag in PlayerClassChoise]
    )
    requiredLvl = models.IntegerField(default=0)  
