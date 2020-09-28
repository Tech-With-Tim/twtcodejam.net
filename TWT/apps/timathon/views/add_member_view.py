from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from ..models.team import Team
from TWT.context import get_discord_context
from django import forms
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
        challenge = Challenge.objects.get(ended=False, posted=True, type='MO')
        user_teams = Team.objects.filter(challenge=challenge, members=user)
        if len(user_teams) != 0:
            messages.add_message(request,
                                 messages.WARNING,
                                 "You are Already in a Team")
            return redirect('/')
        if challenge.team_creation_status == False:
            messages.add_message(request,
                                 messages.WARNING,
                                 "Team creations have closed.")
            return redirect('/')
        team = Team.objects.get(invite=invite)
        team.members.add(user)
        team.save()
        messages.add_message(request,
                             messages.INFO,
                             "Added you in the team!")
        return redirect('timathon:Home')
