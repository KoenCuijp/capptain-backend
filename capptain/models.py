from django.db import models

# Create your models here.
class Match(models.Model):
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
