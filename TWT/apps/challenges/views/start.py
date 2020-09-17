from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from ..context import get_discord_context


class StartView(View):
    """The main landing page for the website."""

    @staticmethod
    def post(request: WSGIRequest, request_id: int) -> HttpResponse:
        """View for ADMINS only to """
        return render(request=request,
                      template_name="challenges/test.html",
                      context=get_discord_context(
                          request=request
                      ))
