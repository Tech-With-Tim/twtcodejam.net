from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views import View
from django.template import RequestContext

from TWT.context import get_discord_context
from ..models import Challenge
from TWT import discord


class DetailView(View):
    """Detailed view of a challenge."""

    @staticmethod
    def get(request: WSGIRequest, challenge_id: int) -> HttpResponse:
        if not request.user.is_authenticated:
            messages.add_message(request,
                                 messages.INFO,
                                 'You are not logged in!')
            return redirect('/')

        challenges = Challenge.objects.filter(id=challenge_id)
        print(len(challenges))
        if not len(challenges):
            return redirect('/')

        context = get_discord_context(request=request)
        context["challenge"] = challenges[0]

        if not challenges[0].posted:
            if not discord.is_staff(member_id=context["user_id"]):
                messages.add_message(request,
                                     messages.INFO,
                                     "You do not have permission to view that!")
                return redirect('/')

        return render(request=request,
                      template_name="challenges/view.html",
                      context=context
                      )
