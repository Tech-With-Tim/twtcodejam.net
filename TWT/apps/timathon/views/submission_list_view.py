from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
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
        if not challenge.voting_status and not context["is_staff"]:
            messages.add_message(request,
                                 messages.INFO,
                                 "The voting period is not open please wait")
            return redirect('timathon:Home')
        submissions = Submission.objects.filter(challenge=challenge)
        paginator = Paginator(submissions, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context["page_obj"] = page_obj
        return render(request, 'timathon/submissions_list.html', context)
