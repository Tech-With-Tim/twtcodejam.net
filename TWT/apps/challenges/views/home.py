"""
Home View
"""
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from TWT.apps.timathon.models.team import Team
from TWT.apps.timathon.models.submission import Submission
from random import randint
from allauth.socialaccount.models import SocialAccount
from TWT.context import get_discord_context
from ..models import Challenge
from django.contrib import messages


class HomeView(View):
    """The main landing page for challenges."""

    def get_context(self, request: WSGIRequest):
        context = get_discord_context(request=request)
        challenges = Challenge.objects.all()
        context["monthly_challenges"] = [challenge for challenge in challenges
                                         if challenge.type == "MO" and challenge.posted and not challenge.ended]
        context["weekly_challenges"] = [challenge for challenge in challenges
                                        if challenge.type == "WE" and challenge.posted and not challenge.ended]
        context["unreleased_challenges"] = {"monthly_challenges": [], "weekly_challenges": []}
        context["ended_challenges"] = {"MO": [], "WE": []}
        for challenge in challenges:
            if challenge.type == "WE" and not challenge.posted:
                context["unreleased_challenges"]["weekly_challenges"].append(challenge)
            if challenge.type == "MO" and not challenge.posted:
                context["unreleased_challenges"]["monthly_challenges"].append(challenge)
            if challenge.ended:  # TODO : Someone pls create view for ended challenges
                context["ended_challenges"][challenge.type].append(challenge)
        context["challenges"] = any((context["monthly_challenges"], context["weekly_challenges"],
                                     context["unreleased_challenges"]["weekly_challenges"],
                                     context["unreleased_challenges"]["monthly_challenges"]))

        return context

    def get(self, request: WSGIRequest) -> HttpResponse:
        context: dict = self.get_context(request=request)
        print(context["challenges"])
        if context["challenges"]:
            print(True)
        try:
            ended_challenges = list(Challenge.objects.filter(ended=True).order_by('-id'))
            ended_challenge = ended_challenges[0]
            ended_winner_1 = Team.objects.get(challenge=ended_challenge, winner=1)
            ended_winner_2 = Team.objects.get(challenge=ended_challenge, winner=2)
            ended_winner_3 = Team.objects.get(challenge=ended_challenge, winner=3)
            winners_old_list = [ended_winner_1, ended_winner_2, ended_winner_3]
            winners = []
            for team in winners_old_list:
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
                team.submission = Submission.objects.get(team=team)
                winners.append(team)
                context["winners"] = winners
                context["ended_codejam"] = True
        except:
            context["ended_codejam"] = False
            print(context)
        if not context["is_verified"]:
            messages.add_message(request,
                                 messages.WARNING,
                                 "You're not verified. Please join our server to continue.")
        return render(request=request,
                      template_name="challenges/index.html",
                      context=context)
