from django.contrib import admin

# Register your models here.
from .models import Team, Player, Position, NFT, Teams_Tournaments

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Position)
admin.site.register(NFT)
admin.site.register(Teams_Tournaments)