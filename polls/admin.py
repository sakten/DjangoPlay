from django.contrib import admin

from .models import Quest, Player, Reward

# Register your models here.
admin.site.register(Quest)
admin.site.register(Player)
admin.site.register(Reward)

