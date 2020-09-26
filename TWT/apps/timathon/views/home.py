from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from TWT.context import get_discord_context
from TWT.apps.challenges.models.challenge import Challenge


class HomeView(View):
    def get_context(self, request: WSGIRequest):
        context = get_discord_context(request=request)
        challenges = Challenge.objects.all()

        context['challenges'] = \
            [challenge for challenge in challenges if challenge.type == Challenge.ChallengeType.MONTHLY]

        context['current_challenge'] = [challenge for challenge in challenges
                                        if challenge.type == Challenge.ChallengeType.MONTHLY and not challenge.ended]

        context['current_challenge'] = context['current_challenge'][0] or None
        print(context)
        return context

    def get(self, request: WSGIRequest) -> HttpResponse:
        context = self.get_context(request)

        if not request.user.is_authenticated:
            return redirect()

        return render(request, template_name='timathon/index.html', context=context)
