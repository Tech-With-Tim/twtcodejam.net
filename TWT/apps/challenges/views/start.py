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

    def post(self, request: WSGIRequest, challenge_id: int):
        if not request.user.is_authenticated:
            messages.add_message(request,
                                 messages.INFO,
                                 'You are not logged in!')
            return redirect('/')

        context = self.get_context(request=request)
        if not context["is_admin"]:
            messages.add_message(request,
                                 messages.INFO,
                                 'You should be an admin to do this!')
            return redirect('/')

        challenge = Challenge.objects.get(id=challenge_id)
        challenge.posted = True
        challenge.save()
        messages.add_message(request,
                             messages.INFO,
                             'Challenge has been posted!')
        return redirect('/')

