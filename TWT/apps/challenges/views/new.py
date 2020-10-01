from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import View

from TWT.context import get_discord_context
from ..models import Challenge

from django import forms


class NewChallengeForm(forms.Form):
    title = forms.CharField(label="Challenge title", max_length=25)
    type = forms.CharField(label="Challenge type")
    short_desc = forms.CharField(label="Short description", max_length=100, required=False)
    description = forms.CharField(label="Full description", max_length=2000)
    rules = forms.CharField(label="Rules", max_length=512)


class NewChallengeView(View):
    """The main landing page for the website."""

    def get_context(self, request: WSGIRequest) -> dict:
        return get_discord_context(request=request)

    def get(self, request: WSGIRequest) -> HttpResponse:
        if not request.user.is_authenticated:
            return redirect('/')

        context = self.get_context(request=request)
        if not context["is_staff"]:
            return redirect('/')
        return render(
            request=request,
            template_name="challenges/new.html",
            context=context
        )

    def post(self, request: WSGIRequest):
        if not request.user.is_authenticated:
            return redirect('/')

        context = self.get_context(request=request)
        if not context["is_staff"]:
            return redirect('/')

        form = NewChallengeForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            type = "WE" if form.cleaned_data["type"] == "Weekly" else "MO"
            description = form.data["description"]
            short_desc = form.cleaned_data["short_desc"]
            if short_desc == "":
                short_desc = description.split('\r\n')[0]
            Challenge.objects.create(
                title=title,
                type=type,
                description=description,
                short_desc=short_desc,
                rules=form.data["rules"],
                author=request.user,
            )
            return redirect('/')

        print("Invalid form")
        return redirect(reverse('home:new'))
