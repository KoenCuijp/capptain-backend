from rest_framework import serializers

from .models import Match


class GetMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = (
            "id",
            "opponent",
            "home_away",
            "location",
            "date",
            "meet_at",
            "starts_at",
            "joining_players",
            "not_joining_players",
            "spectating_players",
            "no_answer_players",
            "created_at",
            "updated_at",
        )


class CreateMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = (
            "opponent",
            "home_away",
            "location",
            "date",
            "meet_at",
            "starts_at",
            "joining_players",
            "not_joining_players",
            "spectating_players",
            "no_answer_players",
        )
