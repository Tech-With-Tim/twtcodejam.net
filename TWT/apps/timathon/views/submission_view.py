from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import View
from TWT.context import get_discord_context
from django import forms

from TWT.discord import client
from ..models.submission import Submission
from ...challenges.models.challenge import Challenge
from ..models.team import Team


class SumbissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['github_link', 'description']

class Submission_View(View):
    def get_context(self, request: WSGIRequest) -> dict:
        return get_discord_context(request=request)

    def post(self, request: WSGIRequest):
        if not request.user.is_authenticated:
            return redirect('/')
        context = self.get_context(request=request)
        form = SumbissionForm(request.POST)
        if form.is_valid():
            description = form.cleaned_data["description"]
            github_link = form.cleaned_data["github_link"]
            challenge = Challenge.objects.get(type='MO', ended=False, posted=True)
            team = get_object_or_404(challenge=challenge, members=request.user) # Team.objects.get(challenge=challenge, members=request.user)
            if len(Submission.objects.filter(challenge=challenge, team=team))!=0:
                messages.add_message(request,
                                     messages.WARNING,
                                     'You have already submitted.')
                client.send_webhook("Submissions", f"<@{context['discord_user'].uid}> tried submitting more than once")
                return redirect(reverse('home:home'))
            Submission.objects.create(
                github_link=github_link,
                description=description,
                team=team,
                challenge=challenge
            )
            team.submitted = True
            team.save()
            messages.add_message(request,
                                 messages.INFO,
                                 'You have successfully submitted your project in the code jam. ')
            client.send_webhook("Submissions", f"<@{context['discord_user'].uid}> submitted their solution")
            return redirect('/')
        print(form.errors)
        print(form["github_link"])
        print("Invalid form")
        messages.add_message(request,
                             messages.WARNING,
                             'Invalid Form')
        return redirect(reverse('timathon:Submission'))

    def get(self, request: WSGIRequest) -> HttpResponse:
        if not request.user.is_authenticated:
            messages.add_message(request,
                                 messages.INFO,
                                 'Sign In')
            return redirect('/')
        context: dict = self.get_context(request=request)
        if not context["is_verified"]:
            return redirect('/')
        try:
            challenge = Challenge.objects.get(ended=False, posted=True, type='MO')
        except Challenge.DoesNotExist:
            messages.add_message(request,
                                 messages.WARNING,
                                 'No ongoing code jam.')
            return redirect('home:home')
        if challenge.submissions_status == False:
            messages.add_message(request,
                                 messages.WARNING,
                                 'Submissions Closed Right Now')
            return redirect('home:home')
        return render(
            request=request,
            template_name="timathon/submit.html",
            context=context
        )