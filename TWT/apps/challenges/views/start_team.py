from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from ..models import Challenge
from TWT.context import get_discord_context
from TWT.discord import client

class StartTeams(View):

    def get_context(self, request: WSGIRequest) -> dict:
        return get_discord_context(request=request)

    def get(self, request: WSGIRequest, challenge_id: int):
        if not request.user.is_authenticated:
            messages.add_message(request,
                                 messages.INFO,
                                 'You are not logged in!')
            return redirect('/')

        context = self.get_context(request=request)
        if not context["is_verified"]:
            return redirect('/')
        if context["is_admin"] or context["is_challenge_host"]:
            challenge = get_object_or_404(Challenge, id=challenge_id)# Challenge.objects.get(id=challenge_id)
            if challenge.submissions_status or challenge.voting_status:
                messages.add_message(request,
                                     messages.WARNING,
                                     'Stop Submission or voting first')
                return redirect('timathon:Home')
            challenge.team_creation_status = True
            challenge.save()
            messages.add_message(request,
                                 messages.INFO,
                                 'Team Creation Has been Started')

            return redirect('timathon:Home')
