from django.contrib import messages
from allauth.socialaccount.models import SocialAccount
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from random import randint, shuffle
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import View
from TWT.context import get_discord_context
from django import forms
from django.core.paginator import Paginator
from TWT.discord import client
from ..models.submission import Submission
from ...challenges.models.challenge import Challenge
from ..models.team import Team

class SubmissionListView(View):
    def get_context(self, request: WSGIRequest) -> dict:
        return get_discord_context(request=request)

    def get(self, request: WSGIRequest):
        if not request.user.is_authenticated:
            return redirect('/')
        context = self.get_context(request=request)
        if not context["is_verified"]:
            return redirect('/')
        try:
            challenge = Challenge.objects.get(ended=False, posted=True, type="MO")
        except Challenge.DoesNotExist:
            messages.add_message(request,
                                 messages.INFO,
                                 "There is no ongoing challenge Right now.")
            return redirect('/')
        if (not context["is_staff"] and challenge.submissions_status) or (not context["is_staff"] and challenge.team_creation_status):
            messages.add_message(request,
                                 messages.INFO,
                                 "The voting period is not open please wait")
            return redirect('timathon:Home')
        submissions = Submission.objects.filter(challenge=challenge)
        submissions = list(submissions)
        if len(submissions) == 0:
            messages.add_message(request,
                                 messages.INFO,
                                 "Nobody has submitted yet")
            return redirect('timathon:Home')
        if not challenge.voting_status and not challenge.team_creation_status and not challenge.submissions_status:
            submissions = Submission.objects.filter(challenge=challenge).order_by('-team__votes')
        else:
            shuffle(submissions)
            user_teams = list(Team.objects.filter(challenge=challenge, members=request.user))
            if not len(user_teams) == 0:
                user_submissions = list(Submission.objects.filter(challenge=challenge, team=user_teams[0]))
                print(user_submissions)
                if not len(user_submissions) == 0:
                    submissions.remove(user_submissions[0])
                    submissions.insert(0,user_submissions[0])

        for submission in submissions:
            team = submission.team
            members = team.members.all()
            discord_members = []
            for member in members:
                new_member = {}
                if member.id == request.user.id:
                    is_in_team = True
                try:
                    user = SocialAccount.objects.get(user_id=member.id)
                except SocialAccount.DoesNotExist:
                    pass
                else:
                    new_member["user_id"] = user.uid
                    avatar_url = user.get_avatar_url()
                    if avatar_url.endswith("None.png"):
                        random = randint(0, 4)
                        avatar_url = f'https://cdn.discordapp.com/embed/avatars/{random}.png'
                    new_member["avatar_url"] = avatar_url
                    new_member["username"] = user.extra_data["username"]
                    new_member["discriminator"] = user.extra_data["discriminator"]
                discord_members.append(new_member)
            team.discord_members = discord_members
            submission.team = team
        context["submissions"] = submissions
        context["challenge"] = challenge
        return render(request, 'timathon/submissions_list.html', context)
