from allauth.socialaccount.models import SocialAccount
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from ..models.team import Team
from TWT.context import get_discord_context
from django import forms
from TWT.discord import client
from ...challenges.models.challenge import Challenge
from django.contrib import messages


class AddMember(View):
    def get_context(self, request: WSGIRequest) -> dict:
        return get_discord_context(request=request)

    def get(self, request: WSGIRequest, invite):
        if not request.user.is_authenticated:
            return redirect('/')
        context = self.get_context(request=request)
        user = request.user
        discord_user = SocialAccount.objects.get(user_id=user.id)
        team = Team.objects.get(invite=invite)
        challenge = Challenge.objects.get(ended=False, posted=True, type='MO')
        user_teams = Team.objects.filter(challenge=challenge, members=user)
        if len(user_teams) != 0:
            messages.add_message(request,
                                 messages.WARNING,
                                 "You are Already in a Team")
            client.send_webhook("Teams", f"<@{discord_user.uid}> tried joining **{team.name}** (ID:{team.ID})",
                                fields=[{"name": "Error", "value": "They are already in a team"}])
            return redirect('/')
        if not challenge.team_creation_status:
            messages.add_message(request,
                                 messages.WARNING,
                                 "Team creations and additions have closed.")
            client.send_webhook("Teams", f"<@{discord_user.uid}> tried joining **{team.name}** (ID:{team.ID})",
                                fields=[{"name": "Error", "value": "Team creations and additions have closed"}])
            return redirect('/')
        if len(team.members.all()) >= 6:
            messages.add_message(request,
                                 messages.WARNING,
                                 "This team is Full.")
            client.send_webhook("Teams", f"<@{discord_user.uid}> tried joining **{team.name}** (ID:{team.ID})",
                                fields=[{"name": "Error", "value": "Team is full"}])
            return redirect('timathon:Home')
        team.members.add(user)
        team.save()
        messages.add_message(request,
                             messages.INFO,
                             f"You have successfully joined {team.name} team")
        client.send_webhook("Teams", f"<@{discord_user.uid}> has successfully joined **{team.name}** (ID:{team.ID})")
        return redirect('timathon:Home')
