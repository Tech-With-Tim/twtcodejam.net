from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View


class Create_team(View):
    def get_context(self, request: WSGIRequest) -> dict:
        pass
        #return get_discord_context(request=request)

    def post(self, request: WSGIRequest):
        #form = YourForm(request.POST)
        #if form.is_valid():
         #   pass
        return redirect('/')

    def get(self, request: WSGIRequest) -> HttpResponse:
        if not request.user.is_authenticated:
            return redirect('/')
        #context = self.get_context(request=request)
        return render(
            request=request,
            template_name="timathon/create_teams.html",
            #context=context
        )
