# Directory Structure of the source code of the code jam repo

The following is the directory structure for the code jam website for easier understanding of the code base


```
├── CONTRIBUTE.md
├── Dockerfile
├── LICENSE
├── README.md
├── SETUP.md
├── STRUCTURE.md
├── TWT
│   ├── __init__.py
│   ├── apps
│   │   ├── challenges
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── migrations
│   │   │   │   ├── 0001_initial.py
│   │   │   │   ├── 0002_challenge_ended.py
│   │   │   │   ├── 0003_auto_20200926_0331.py
│   │   │   │   ├── 0004_team.py
│   │   │   │   ├── 0005_auto_20200926_1741.py
│   │   │   │   ├── 0006_delete_team.py
│   │   │   │   ├── 0007_challenge_status.py
│   │   │   │   ├── 0008_auto_20200929_0004.py
│   │   │   │   ├── 0009_challenge_voting_status.py
│   │   │   │   ├── 0010_challenge_members_voted.py
│   │   │   │   ├── 0011_auto_20201005_1657.py
│   │   │   │   ├── 0012_remove_challenge_members_voted.py
│   │   │   │   ├── 0013_auto_20201006_1749.py
│   │   │   │   ├── 0014_custompage.py
│   │   │   │   ├── 0015_auto_20201010_0224.py
│   │   │   │   ├── 0016_custompage_page_menu_name.py
│   │   │   │   └── __init__.py
│   │   │   ├── models
│   │   │   │   ├── __init__.py
│   │   │   │   ├── challenge.py
│   │   │   │   └── custom_pages.py
│   │   │   ├── urls.py
│   │   │   └── views
│   │   │       ├── __init__.py
│   │   │       ├── custom_page_view.py
│   │   │       ├── delete_challenge.py
│   │   │       ├── end.py
│   │   │       ├── home.py
│   │   │       ├── logout.py
│   │   │       ├── new.py
│   │   │       ├── start.py
│   │   │       ├── start_submission.py
│   │   │       ├── start_team.py
│   │   │       ├── start_voting.py
│   │   │       ├── stop_submission.py
│   │   │       ├── stop_team.py
│   │   │       ├── stop_voting.py
│   │   │       ├── test.py
│   │   │       ├── unreleased.py
│   │   │       └── view.py
│   │   ├── timathon
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── migrations
│   │   │   │   ├── 0001_initial.py
│   │   │   │   ├── 0002_team_votes.py
│   │   │   │   ├── 0003_submission_challenge.py
│   │   │   │   ├── 0004_team_voted_by.py
│   │   │   │   ├── 0005_auto_20201006_0128.py
│   │   │   │   ├── 0006_auto_20201006_0131.py
│   │   │   │   ├── 0007_auto_20201006_0137.py
│   │   │   │   ├── 0008_auto_20201006_0229.py
│   │   │   │   ├── 0009_auto_20201020_0030.py
│   │   │   │   ├── 0010_auto_20201020_0033.py
│   │   │   │   └── __init__.py
│   │   │   ├── models
│   │   │   │   ├── __init__.py
│   │   │   │   ├── submission.py
│   │   │   │   └── team.py
│   │   │   ├── urls.py
│   │   │   └── views
│   │   │       ├── __init__.py
│   │   │       ├── add_member_view.py
│   │   │       ├── codjam_listview.py
│   │   │       ├── create_team.py
│   │   │       ├── home.py
│   │   │       ├── leave_member_view.py
│   │   │       ├── submission_list_view.py
│   │   │       ├── submission_view.py
│   │   │       ├── unvote.py
│   │   │       ├── view_team.py
│   │   │       └── vote.py
│   │   └── weekly
│   │       ├── __init__.py
│   │       ├── admin.py
│   │       ├── migrations
│   │       │   └── __init__.py
│   │       ├── models
│   │       │   └── __init__.py
│   │       ├── sample-tester.py
│   │       ├── urls.py
│   │       └── views
│   │           ├── __init__.py
│   │           └── home.py
│   ├── asgi.py
│   ├── cache.py
│   ├── context.py
│   ├── discord.py
│   ├── settings.py
│   ├── static
│   │   ├── css
│   │   │   ├── base.css
│   │   │   ├── bootstrap.min.css
│   │   │   ├── index.css
│   │   │   ├── logout.css
│   │   │   ├── new.css
│   │   │   ├── submissions_list.css
│   │   │   ├── timathonHome.css
│   │   │   └── timathonTeam.css
│   │   ├── images
│   │   │   ├── cropped-Tech-With-TimXL-192x192.png
│   │   │   └── discord.png
│   │   └── js
│   │       ├── bootstrap.min.js
│   │       ├── jquery-3.3.1.slim.min.js
│   │       └── popper.min.js
│   ├── templates
│   │   ├── base
│   │   │   ├── base.html
│   │   │   └── navbar.html
│   │   ├── challenges
│   │   │   ├── custom_page.html
│   │   │   ├── index.html
│   │   │   ├── logout.html
│   │   │   ├── new.html
│   │   │   ├── test.html
│   │   │   ├── unreleased.html
│   │   │   └── view.html
│   │   ├── timathon
│   │   │   ├── create_teams.html
│   │   │   ├── index.html
│   │   │   ├── submissions_list.html
│   │   │   ├── submit.html
│   │   │   └── view_team.html
│   │   └── weekly
│   │       └── index.html
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── manage.py
├── nginx.default
├── our_secrets.example.py
├── requirements.txt
└── start-server.sh
```