from allauth.socialaccount.models import SocialAccount
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from ..models import Team, Submission
from TWT.context import get_discord_context
from django import forms
from TWT.discord import client
from ...challenges.models.challenge import Challenge
from django.contrib import messages


class Vote(View):
    def get_context(self, request: WSGIRequest) -> dict:
        return get_discord_context(request=request)

    def get(self, request: WSGIRequest, teamid):
        if not request.user.is_authenticated:
            return redirect('/')
        context = self.get_context(request=request)
        if not context["is_verified"]:
            return redirect('/')
        user = request.user
        discord_user = context['discord_user']
        team = get_object_or_404(Team, ID=teamid) # Team.objects.get(invite=invite)
        challenge = get_object_or_404(Challenge, ended=False, posted=True, type='MO')#Challenge.objects.get(ended=False, posted=True, type='MO')
        user_teams = Team.objects.filter(challenge=challenge, members=user)
        user_voted_teams = Team.objects.filter(challenge=challenge, voted_by=user)
        if len(user_teams) == 0:
            messages.add_message(request,
                                 messages.WARNING,
                                 "You have not participated in the code jam")
            client.send_webhook("Teams", f"<@{discord_user.uid}> tried voting **{team.name}** (ID:{team.ID})",
                                fields=[{"name": "Error", "value": "They have not particpated in the code jam"}])
            return redirect('/')
        if len(Submission.objects.filter(challenge=challenge,team=user_teams[0])) == 0:
            messages.add_message(request,
                                 messages.WARNING,
                                 "You have not Submitted a project in the code jam")
            client.send_webhook("Teams", f"<@{discord_user.uid}> tried voting **{team.name}** (ID:{team.ID})",
                                fields=[{"name": "Error", "value": "They have not Submitted a project in the code jam"}])
            return redirect('/')
        if len(user_voted_teams) >= 3:
            messages.add_message(request,
                                 messages.WARNING,
                                 "You have exceeded your amount of votes.")
            client.send_webhook("Teams", f"<@{discord_user.uid}> tried voting **{team.name}** (ID:{team.ID})",
                                fields=[{"name": "Error", "value": "They have exceeded their amount of votes"}])
            return redirect('/')
        if team in user_teams:
            messages.add_message(request,
                                 messages.WARNING,
                                 "You Cannot vote for yourself.")
            client.send_webhook("Teams", f"<@{discord_user.uid}> tried voting **{team.name}** (ID:{team.ID})",
                                fields=[{"name": "Error", "value": "User is in the in the team"}])
            return redirect('/')
        if team in user_voted_teams:
            messages.add_message(request,
                                 messages.WARNING,
                                 "You Cannot vote this team again.")
            client.send_webhook("Teams", f"<@{discord_user.uid}> tried voting **{team.name}** (ID:{team.ID})",
                                fields=[{"name": "Error", "value": "User has already voted the team"}])
            return redirect('/')

        if not challenge.voting_status:
            messages.add_message(request,
                                 messages.WARNING,
                                 "Challenge Voting is not open.")
            client.send_webhook("Teams", f"<@{discord_user.uid}> tried voting **{team.name}** (ID:{team.ID})",
                                fields=[{"name": "Error", "value": "Challenge Voting is not open."}])
            return redirect('/')
        team.votes = team.votes +1
        team.voted_by.add(user)
        team.save()
        messages.add_message(request,
                             messages.WARNING,
                             f"You have successfully voted {team.name}")
        client.send_webhook("Teams", f"<@{discord_user.uid}> Voted **{team.name}** (ID:{team.ID})")
        return redirect('timathon:Home')
