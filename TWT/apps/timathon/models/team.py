from django.db import models
from django.contrib.auth.models import User
import uuid

from TWT.apps.challenges.models import Challenge


class Team(models.Model):
    class Postion(models.IntegerChoices):
        FIRST = 1
        SECOND = 2
        THIRD = 3
        NOT_WINNER = 0
    ID = models.AutoField(primary_key=True)
    invite = models.CharField(max_length=255, unique=True, editable=False, default=uuid.uuid4,
                          help_text="invite")

    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, help_text="Code Jam")
    name = models.TextField(max_length=50, help_text="Name of the team")

    created_at = models.DateTimeField(auto_now=True)
    winner = models.IntegerField(choices=Postion.choices, default=Postion.NOT_WINNER)
    submitted = models.BooleanField(default=False)
    votes = models.IntegerField(default=0)
    members = models.ManyToManyField(User)
    voted_by = models.ManyToManyField(User, related_name='userwhovotedforteam', blank=True)

    def __str__(self):
        return f"Team {self.ID} ({self.name}) for challenge {self.challenge.id}"

