from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from ..models import Challenge
from TWT.context import get_discord_context


class StopTeams(View):

    def get_context(self, request: WSGIRequest) -> dict:
        return get_discord_context(request=request)

    def get(self, request: WSGIRequest, challenge_id: int):
        if not request.user.is_authenticated:
            messages.add_message(request,
                                 messages.INFO,
                                 'You are not logged in!')
            return redirect('/')

        context = self.get_context(request=request)
        if context["is_admin"] or context["is_challenge_host"]:
            challenge = Challenge.objects.get(id=challenge_id)
            challenge.team_creation_status = False
            challenge.save()
            messages.add_message(request,
                                 messages.INFO,
                                 'Team Creation Has been stopped')
            return redirect('/')
