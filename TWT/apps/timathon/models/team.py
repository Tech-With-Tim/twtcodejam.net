from django.db import models
from django.contrib.auth.models import User
import uuid

from TWT.apps.challenges.models import Challenge


class Team(models.Model):
    ID = models.AutoField(primary_key=True)
    invite = models.CharField(max_length=255, unique=True, editable=False, default=uuid.uuid4,
                          help_text="invite")

    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, help_text="Code Jam")
    name = models.TextField(max_length=50, help_text="Name of the team")

    created_at = models.DateTimeField(auto_now=True)
    winner = models.BooleanField(default=False)
    submitted = models.BooleanField(default=False)

    members = models.ManyToManyField(User)

    def __str__(self):
        return f"Team {self.ID} ({self.name}) for challenge {self.challenge.id}"

