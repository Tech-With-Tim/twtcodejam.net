from django.contrib import admin

from TWT.apps.timathon.models.team import Team
from TWT.apps.timathon.models.submission import Submission

admin.site.register(Team)
admin.site.register(Submission)