from django.contrib import admin

# Register your models here.
from .models import Player, Bet

class PlayerAdmin(admin.ModelAdmin):
	fields = ['netid', 'balance', 'committed', 'friendlist']

class BetAdmin(admin.ModelAdmin):
	fields = ['name', 'description', 'value', 'category', 'status', 'expdate', 'creator', 'taker', 'arbitrator']


admin.site.register(Player, PlayerAdmin)
admin.site.register(Bet, BetAdmin)