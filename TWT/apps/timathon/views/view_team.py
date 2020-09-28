from allauth.socialaccount.models import SocialAccount
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from TWT.apps.challenges.models import Challenge
from TWT.apps.timathon.models import Team
from TWT.context import get_discord_context


class View_teams(View):
    def get_context(self, request: WSGIRequest) -> dict:
        context = get_discord_context(request)
        challenges = list(Challenge.objects.filter(ended=False, type=Challenge.ChallengeType.MONTHLY))
        if not context['is_staff']:
            challenges = filter(lambda x: x.posted, challenges)
        print(challenges)
        if len(challenges) > 0:
            print(challenges)
            current_challenge = challenges[0]
            context['challenge'] = current_challenge
            old_teams = Team.objects.filter(challenge_id=current_challenge.id)
            teams = []
            for team in old_teams:
                members = team.members.all()
                discord_members = []
                for member in members:
                    new_member = {}
                    try:
                        user = SocialAccount.objects.get(user_id=member.id)
                    except SocialAccount.DoesNotExist:
                        pass
                    else:
                        new_member["user_id"] = user.uid
                        new_member["avatar_url"] = user.get_avatar_url()
                        new_member["username"] = user.extra_data["username"]
                        new_member["discriminator"] = user.extra_data["discriminator"]
                    discord_members.append(new_member)
                team.discord_members = discord_members
                teams.append(team)

            print(teams)

            context['teams'] = teams

        return context

    def post(self, request: WSGIRequest):
        # form = request(request.POST)
        # if form.is_valid():
        #    pass
        return redirect('/')

    def get(self, request: WSGIRequest) -> HttpResponse:
        if not request.user.is_authenticated:
            return redirect('/')
        context = self.get_context(request=request)
        return render(
            request=request,
            template_name="timathon/view_team.html",
            context=context
        )
