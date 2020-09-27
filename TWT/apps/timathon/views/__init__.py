from .home import HomeView
from .create_team import Create_team
from .view_teams import View_teams
from .submission_view import Submission_View
home = HomeView.as_view()
create_team = Create_team.as_view()
view_teams = View_teams.as_view()
submission = Submission_View.as_view()