"""
this is being called by a button that is why we are using a get request
this is to end a challenge either weekly or monthly from the integer id
"""
from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from ..models import Challenge
from TWT.context import get_discord_context


class DeleteView(View):
    """View for ending a challenge"""

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
            challenge = get_object_or_404(Challenge, id=challenge_id)
            challenge.delete()
            messages.add_message(request,
                                 messages.INFO,
                                 'Challenge has been deleted!')
            return redirect('home:unreleased')

        else:
            messages.add_message(request,
                                 messages.INFO,
                                 'You should be an admin or challenge host to do this!')
            return redirect('/')
