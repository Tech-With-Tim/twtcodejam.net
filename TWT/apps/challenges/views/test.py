from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from TWT.context import get_discord_context


class TestView(View):
    """The main landing page for the website."""

    @staticmethod
    def get(request: WSGIRequest) -> HttpResponse:
        return render(request=request,
                      template_name="challenges/test.html",
                      context=get_discord_context(
                          request=request
                      ))
