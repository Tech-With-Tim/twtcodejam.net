from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from ..models.team import Team
from TWT.context import get_discord_context
from django import forms
from ...challenges.models.challenge import Challenge
from django.contrib import messages


class LeaveTeam(View):
    def get_context(self, request: WSGIRequest) -> dict:
        return get_discord_context(request=request)

    def get(self, request: WSGIRequest):
        if not request.user.is_authenticated:
            return redirect('/')
        context = self.get_context(request=request)
        user = request.user
        challenge = Challenge.objects.get(ended=False, posted=True, type='MO')
        if len(Team.objects.filter(challenge=challenge, members=user)) <= 0:
            messages.add_message(request,
                                 messages.WARNING,
                                 "You are not in a team !")
            return redirect('timathon:Home')
        team = Team.objects.get(challenge=challenge, members=user)
        team.members.remove(user)
        team.save()
        messages.add_message(request,
                             messages.INFO,
                             "Removed you from the team!")
        return redirect('timathon:Home')
