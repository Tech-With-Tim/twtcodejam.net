from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views import View

from allauth.account.adapter import get_adapter

from ..context import get_discord_context


class LogoutView(View):
    """The main landing page for the website."""

    @staticmethod
    def get(request: WSGIRequest) -> HttpResponse:
        if not request.user.is_authenticated:
            messages.add_message(request,
                                 messages.INFO,
                                 'You are already logged out!',
                                 extra_tags='alert alert-primary')
            return redirect('/')

        return render(request=request,
                      template_name="challenges/logout.html",
                      context=get_discord_context(
                          request=request
                      ))

    def post(self, request: WSGIRequest) -> HttpResponse:
        if request.user.is_authenticated:
            self.logout(request=request)
            return redirect('/')

    def logout(self, request: WSGIRequest) -> None:
        adapter = get_adapter(request=request)
        adapter.add_message(
            self.request,
            messages.SUCCESS,
            'Logged out!',
        )
        adapter.logout(request=request)
