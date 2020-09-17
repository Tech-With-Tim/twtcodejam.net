from .home import HomeView
from .logout import LogoutView
from .new import NewChallengeView
from .view import DetailView
from .test import TestView
from .end import EndView
from .start import StartView

start = EndView.as_view()
end = EndView.as_view()
test = TestView.as_view()
logout = LogoutView.as_view()
new = NewChallengeView.as_view()
view = DetailView.as_view()
