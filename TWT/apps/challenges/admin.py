from django.contrib import admin
from .models.challenge import Challenge
from .models.custom_pages import CustomPage
admin.site.register(Challenge)
admin.site.register(CustomPage)
