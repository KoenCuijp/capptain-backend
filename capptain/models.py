from enum import StrEnum

from django.contrib.auth.models import User
from django.db import models


class Team(models.Model):
    """Represent a sports team."""

    name = models.CharField(max_length=40)
    address = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PlayerRole(StrEnum):
    CAPTAIN = "Captain"
    PLAYER = "Player"


class TeamPlayer(models.Model):
    """Represent a player in a team. A player can be in multiple teams."""

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=20,
        choices=[(role.name, role.value) for role in PlayerRole],
    )


class Match(models.Model):
    """Represent a match between two teams."""

    opponent = models.CharField(max_length=50)
    home_away = models.CharField(
        max_length=1, choices=[("H", "Home Game"), ("A", "Away Game")]
    )
    location = models.CharField(max_length=50)
    date = models.DateField()
    meet_at = models.TimeField()
    starts_at = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Matches"
