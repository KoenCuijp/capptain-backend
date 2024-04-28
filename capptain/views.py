from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpRequest
from rest_framework import permissions, response, status, views
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Match, Team, TeamPlayer
from .serializers import CreateMatchSerializer, GetMatchSerializer


# View for Capptain-specific objects
class GetMatchesView(APIView):
    serializer_class = GetMatchSerializer

    def get(self, request: HttpRequest) -> Response:
        all_matches = Match.objects.all()

        if not all_matches:
            return Response(
                {"error": "No matches found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Serialize the data
        serializer = self.serializer_class(all_matches, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


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
    serializer_class = CreateMatchSerializer

    def post(self, request: HttpRequest) -> Response:
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            return Response(
                {"error": "invalid payload"}, status=status.HTTP_400_BAD_REQUEST
            )

        team_id = serializer.data.get("team")
        team = Team.objects.get(id=team_id)
        opponent = serializer.data.get("opponent")
        home_away = serializer.data.get("home_away")
        location = serializer.data.get("location")
        date = serializer.data.get("date")
        meet_at = serializer.data.get("meet_at")
        starts_at = serializer.data.get("starts_at")

        match = Match(
            team=team,
            opponent=opponent,
            home_away=home_away,
            location=location,
            date=date,
            meet_at=meet_at,
            starts_at=starts_at,
        )

        match.save()

        # On creation of a match, no players have answered yet
        no_answer_players = TeamPlayer.objects.filter(team=team)
        match.no_answer_players.set(no_answer_players)

        match.save()

        return Response(GetMatchSerializer(match).data, status=status.HTTP_201_CREATED)


# Login & Register flow views
class RegisterView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request: HttpRequest) -> response.Response:
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            return response.Response(
                {"error": "Username and password required"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user = User.objects.create_user(username=username, password=password)
        return response.Response(
            {"message": f"User created {user.email}"}, status=status.HTTP_201_CREATED
        )


class LoginView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request: HttpRequest) -> response.Response:
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return response.Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return response.Response(
                {"error": "Invalid username or password"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class LogoutView(views.APIView):
    def post(self, request: HttpRequest) -> response.Response:
        logout(request)
        return response.Response({"message": "Logged out"}, status=status.HTTP_200_OK)
