from .home import HomeView
from .logout import LogoutView
from .new import NewChallengeView
from .view import DetailView
from .test import TestView
from .end import EndView
from .start import StartView
from .stop_team import StopTeams
from .start_submission import StartSubmission
from .stop_submission import StopSubmission
start = StartView.as_view()
end = EndView.as_view()
test = TestView.as_view()
logout = LogoutView.as_view()
new = NewChallengeView.as_view()
view = DetailView.as_view()
stop_team = StopTeams.as_view()
start_submission = StartSubmission.as_view()
stop_submission = StopSubmission.as_view()