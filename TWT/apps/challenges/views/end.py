"""
View for ending a code jam
"""
from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from ..models import Challenge
from TWT.context import get_discord_context
from TWT.discord import client
from TWT.apps.timathon.models.team import Team


class EndView(View):
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
            challenge = get_object_or_404(Challenge, id=challenge_id) # Challenge.objects.get(id=challenge_id)
            try:
                winners = [Team.objects.get(challenge=challenge,winner=i) for i in range(1,4)]
            except Team.DoesNotExist:
                messages.add_message(request,
                                     messages.WARNING,
                                     'Declare the winning team first')
                return redirect('timathon:Home')
            challenge.ended = True
            challenge.status = "ENDED"
            challenge.team_creation_status = False
            challenge.submissions_status = False
            challenge.save()
            messages.add_message(request,
                                 messages.INFO,
                                 'Challenge has been closed!')
            client.send_webhook("Code Jam", f"<@{context['discord_user'].uid}> has ended the codejam. Thanks for participating",
                                fields=[{"name": "Link", "value": f"[Visit]({request.build_absolute_uri('/')})"}])
            client.send_webhook("Timathon", f"Timathon has ended. Thanks for participating",
                                fields=[{"name": "Link", "value": f"[Visit]({request.build_absolute_uri('/')})"}], codeJam=True)
            return redirect('/')

        else:
            messages.add_message(request,
                                 messages.INFO,
                                 'You should be an admin or challenge host to do this!')
            return redirect('/')
