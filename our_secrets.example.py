"""
We need to use `our_secrets` since django has a `secrets.py` file somewhere.

Make a new file for your own secrets, named `our_secrets`. Put the following variables in here:
"""
# generate secret key from django console read the docs on how to do it
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
dsn = "dsn"  # for sentry integration not compulsory if not then comment lines 194-202 in settings.py
CODEJAM_WEBHOOK = "URL"
CODEJAM_INFO_CHANNEL_WEBHOOK = "URL"