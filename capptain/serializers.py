from typing import Any

from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from .models import Match, Team, TeamPlayer


class DynamicFieldsModelSerializer(ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.

    see: https://www.django-rest-framework.org/api-guide/serializers/#example
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop("fields", None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class UserSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class TeamSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class TeamPlayerSerializer(DynamicFieldsModelSerializer):
    player = UserSerializer(fields=("username",))

    class Meta:
        model = TeamPlayer
        fields = "__all__"


class GetMatchSerializer(DynamicFieldsModelSerializer):
    team = TeamSerializer()
    joining_players = TeamPlayerSerializer(many=True)
    not_joining_players = TeamPlayerSerializer(many=True)
    spectating_players = TeamPlayerSerializer(many=True)
    no_answer_players = TeamPlayerSerializer(many=True)

    class Meta:
        model = Match
        fields = "__all__"


class CreateMatchSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Match
        fields = (
            "team",
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

        def validate(self, data: dict[str, Any]) -> dict[str, Any]:
            # TODO: check player attendance lists:
            # https://www.django-rest-framework.org/api-guide/serializers/#object-level-validation
            return data
