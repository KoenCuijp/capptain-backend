from django.http import HttpRequest
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Match
from .serializers import CreateMatchSarializer, GetMatchSerializer


# Create your views here.
class GetMatchesView(APIView):
    all_matches = Match.objects.all()
    serializer_class = GetMatchSerializer

    def get(self, request: HttpRequest) -> Response:
        ...


class GetMatchView(APIView):
    serializer_class = GetMatchSerializer
    http_method_names = ["get", "put"]

    def get(self, request: HttpRequest, match_id: str | None) -> Response:
        if match_id is None:
            return Response(
                {"error": "no match ID provided"}, status=status.HTTP_400_BAD_REQUEST
            )

        match = Match.objects.filter(id=match_id)

        if not match:
            return Response(
                {"error": f"No match found for id {match_id}"},
                status=status.HTTP_404_NOT_FOUND,
            )

        match_data = GetMatchSerializer(match[0]).data
        return Response(match_data, status=status.HTTP_200_OK)


class CreateMatchView(APIView):
    serializer_class = CreateMatchSarializer

    def post(self, request: HttpRequest) -> Response:
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(
                {"error": "invalid payload"}, status=status.HTTP_400_BAD_REQUEST
            )

        opponent = serializer.data.get("opponent")
        home_away = serializer.data.get("home_away")
        location = serializer.data.get("location")
        date = serializer.data.get("date")
        meet_at = serializer.data.get("meet_at")
        starts_at = serializer.data.get("starts_at")

        match = Match(
            opponent=opponent,
            home_away=home_away,
            location=location,
            date=date,
            meet_at=meet_at,
            starts_at=starts_at,
        )
        match.save()

        return Response(GetMatchSerializer(match).data, status=status.HTTP_201_CREATED)
