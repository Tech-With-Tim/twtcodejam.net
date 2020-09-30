from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from ..models import Challenge
from TWT.context import get_discord_context


class StartView(View):
    """Starts a challenge"""

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
            ongoing_challenges = Challenge.objects.filter(type='MO', ended=False, posted=True)
            if len(ongoing_challenges) >0:
                messages.add_message(request,
                                     messages.INFO,
                                     'There is already a challenge going on')
                return redirect('timathon:Home')
            challenge = Challenge.objects.get(id=challenge_id)
            challenge.posted = True
            challenge.status = "RUNNING"
            challenge.team_creation_status = True
            challenge.save()
            messages.add_message(request,
                                 messages.INFO,
                                 'Challenge has been posted!')
            return redirect('/')

        else:
            messages.add_message(request,
                                 messages.INFO,
                                 'You should be an admin or challenge host to do this!')
            return redirect('/')
