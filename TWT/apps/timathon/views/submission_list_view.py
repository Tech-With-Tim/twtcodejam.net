from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import View
from TWT.context import get_discord_context
from django import forms
from django.views.generic import ListView
from TWT.discord import client
from ..models.submission import Submission
from ...challenges.models.challenge import Challenge
from ..models.team import Team