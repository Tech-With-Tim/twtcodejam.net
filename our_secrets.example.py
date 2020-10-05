"""
We need to use `our_secrets` since django has a `secrets.py` file somewhere.

Make a new file for your own secrets, named `our_secrets`. Put the following variables in here:
"""

SECRET_KEY = 'Your secret key'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # your database
        'NAME': 'your-database-name',
        'USER': 'your-user',
        'PASSWORD': 'your-password',
        'HOST': 'your-host'
    }
}

ALLOWED_HOSTS = ['your-hosts']


# Discord stuff
TOKEN: str = "your bot token."  # > https://discord.com/developers/applications
LOG_WEBHOOK = "url"
CODEJAM_WEBHOOK = "URL"