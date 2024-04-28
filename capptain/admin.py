from django.contrib import admin

from .models import Match, Team, TeamPlayer

admin.site.register([Match, Team, TeamPlayer])
