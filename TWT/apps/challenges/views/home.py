from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from TWT.context import get_discord_context
from ..models import Challenge


class HomeView(View):
    """The main landing page for challenges."""

    def get_context(self, request: WSGIRequest):
        context = get_discord_context(request=request)
        challenges = Challenge.objects.all()
        context["monthly_challenges"] = [challenge for challenge in challenges
                                         if challenge.type == "MO" and challenge.posted]
        context["weekly_challenges"] = [challenge for challenge in challenges
                                        if challenge.type == "WE" and challenge.posted]
        context["unreleased_challenges"] = {"monthly_challenges": [], "weekly_challenges": []}

        for challenge in challenges:
            if challenge.type == "WE" and not challenge.posted:
                context["unreleased_challenges"]["weekly_challenges"].append(challenge)
            if challenge.type == "MO" and not challenge.posted:
                context["unreleased_challenges"]["monthly_challenges"].append(challenge)

        context["challenges"] = any((context["monthly_challenges"], context["weekly_challenges"],
                                     context["unreleased_challenges"]["weekly_challenges"],
                                     context["unreleased_challenges"]["weekly_challenges"]))

        return context

    def get(self, request: WSGIRequest) -> HttpResponse:
        context: dict = self.get_context(request=request)

        return render(request=request,
                      template_name="challenges/index.html",
                      context=context)
