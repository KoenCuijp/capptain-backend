from django.urls import path

from .views import CreateMatchView, GetMatchesView, GetMatchView

urlpatterns = [
    path("matches", GetMatchesView.as_view()),
    path("create-match", CreateMatchView.as_view()),
    path("match/<int:match_id>", GetMatchView.as_view()),
]
