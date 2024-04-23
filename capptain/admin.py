from django.contrib import admin

from .models import Match, Team, TeamPlayer

admin.site.register(Match)
admin.site.register(Team)
admin.site.register(TeamPlayer)
