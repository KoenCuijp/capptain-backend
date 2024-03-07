from django.urls import path

from .views import CreateMatchView, GetMatchesView, GetMatchView

urlpatterns = [
    path("matches", GetMatchesView.as_view(), name="matches"),
    path("create-match", CreateMatchView.as_view(), name="create-match"),
    path("match/<int:match_id>", GetMatchView.as_view(), name="match"),
]
