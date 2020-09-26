from django.db import models
from django.contrib.auth.models import User
import uuid

from TWT.apps.challenges.models import Challenge


class Team(models.Model):
    id = models.CharField(max_length=255, primary_key=True, unique=True, editable=False, default=uuid.uuid4,
                          help_text="Team id")

    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, help_text="Code Jam")
    name = models.TextField(max_length=50, help_text="Name of the team")

    created_at = models.DateTimeField(auto_now=True)
    winner = models.BooleanField()

    members = models.ManyToManyField(User)

    def __str__(self):
        return f"Team {self.id} for challenge {self.challenge.id}"

