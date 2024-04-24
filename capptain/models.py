from enum import StrEnum

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

from .model_mixins import ValidateModelMixin


class Team(models.Model):
    """Represent a sports team"""

    name = models.CharField(max_length=40)
    address = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class PlayerRole(StrEnum):
    CAPTAIN = "Captain"
    PLAYER = "Player"


class TeamPlayer(models.Model):
    """Represent a player in a team, a player can be in multiple teams"""

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=20,
        choices=[(role.name, role.value) for role in PlayerRole],
    )

    def __str__(self) -> str:
        return f"{self.player.username} ({self.role} of {self.team.name})"


class Match(models.Model, ValidateModelMixin):
    """Represent a match between two teams"""

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    opponent = models.CharField(max_length=50)
    home_away = models.CharField(
        max_length=1, choices=[("H", "Home Game"), ("A", "Away Game")]
    )
    location = models.CharField(max_length=50)
    date = models.DateField()
    meet_at = models.TimeField()
    starts_at = models.TimeField()
    joining_players = models.ManyToManyField(TeamPlayer, related_name="joining_players")
    not_joining_players = models.ManyToManyField(
        TeamPlayer, related_name="not_joining_players"
    )
    spectating_players = models.ManyToManyField(
        TeamPlayer, related_name="spectating_players"
    )
    no_answer_players = models.ManyToManyField(
        TeamPlayer, related_name="no_answer_players"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Matches"

    def __str__(self) -> str:
        return f"[{self.home_away}] {self.opponent} ({self.date})"

    def clean(self) -> None:
        """
        Add custom validation for the model
        """
        super().clean()

        if self.meet_at >= self.starts_at:
            raise ValidationError("Match must start after the meeting time")

        if self.team.name == self.opponent:
            raise ValidationError("Team cannot play against itself")

        joining_players = [player.id for player in self.joining_players.all()]
        not_joining_players = [player.id for player in self.not_joining_players.all()]
        spectating_players = [player.id for player in self.spectating_players.all()]
        no_answer_players = [player.id for player in self.no_answer_players.all()]
        all_players = (
            joining_players
            + not_joining_players
            + spectating_players
            + no_answer_players
        )
        all_players_unique = set(all_players)

        if len(all_players) != len(all_players_unique):
            raise ValidationError("Players cannot be in multiple attendance lists")

        if len(all_players) != len(self.team.teamplayer_set.all()):
            raise ValidationError("Not all TeamPlayers are listed in attendance lists")
