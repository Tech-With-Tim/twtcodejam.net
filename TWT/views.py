from django.contrib import messages
from django.shortcuts import redirect

"""
Custom error handlers here
"""
def handler404(request, exception):
    messages.add_message(request,
                         messages.WARNING,
                         "That page does not exist")
    return redirect('/')
def handler500(request):
    messages.add_message(request,
                         messages.WARNING,
                         "Something unexpected occurred.")
    return redirect('/')
