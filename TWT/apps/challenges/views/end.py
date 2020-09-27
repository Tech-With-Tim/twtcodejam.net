from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from ..models import Challenge
from TWT.context import get_discord_context


class EndView(View):
    """View for ending a challenge"""

    def get_context(self, request: WSGIRequest) -> dict:
        return get_discord_context(request=request)

    def post(self, request: WSGIRequest, challenge_id: int):
        if not request.user.is_authenticated:
            messages.add_message(request,
                                 messages.INFO,
                                 'You are not logged in!')
            return redirect('/')

        context = self.get_context(request=request)
        if context["is_admin"] or context["is_challenge_host"]:
            challenge = Challenge.objects.get(id=challenge_id)
            challenge.ended = True
            challenge.save()
            messages.add_message(request,
                                 messages.INFO,
                                 'Challenge has been closed!')
            return redirect('/')

        else:
            messages.add_message(request,
                                 messages.INFO,
                                 'You should be an admin or challenge host to do this!')
            return redirect('/')
