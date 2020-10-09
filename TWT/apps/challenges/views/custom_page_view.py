from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from TWT.context import get_discord_context
from TWT.apps.challenges.models.custom_pages import CustomPage

class CustomView(View):
    def get_context(self, request: WSGIRequest):
        context = get_discord_context(request=request)
        return context
    def get(self, request: WSGIRequest, link_name):
        context: dict = self.get_context(request=request)
        #CustomPage.objects.get()
        page = get_object_or_404(CustomPage, linkName=link_name)
        if page.only_staff or not page.public:
            if not context["is_staff"]:
                messages.add_message(request,
                                     messages.WARNING,
                                     'You dont have permissions to view')
                return redirect('/')
        context["page"] = page
        return render(request=request,
                      template_name='challenges/custom_page.html',
                      context=context)