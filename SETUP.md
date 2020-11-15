# Setup

## Steps:

- First fork this repository and Clone your fork
- after that checkout to the dev branch
```shell script
git checkout dev
```
- Now to set the website up you have to create a file called our_secrets.py, copy everything from our_secrets.example.py and paste it here
** **
- I have explained everything in the comments for the postgres database either you can setup on a local postgres db or for ease of use you can setup on heroku. I recommend setting up on local machine as heroku users face problems.
- To generate a secret key run this in a python shell
In Shell:
```shell script
python
```
```python
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```
** **
* Now open TWT/settings.py and turn `DEBUG = True`

* Open TWT/discord.py and edit the guild_id in lines 79, 82, 85 according to your server
* edit all the role ids in lines 89-95

** **
* `Now run python manage.py makemigrations`
* `python manage.py migrate`
** **
- run `python manage.py createsuperuser` <br>
- go to http://127.0.0.1:8000/admin  and sign in with the account u created <br>
- go to Sites Section in the and edit the existing record and the site would be 
 localhost and localhost in both the rows
- go to https://discord.com/developers/applications and create a new application for this server
- Go to the application (open application which has the bot you used in your our_secrets.py file and make sure to add the bot to your server where all the roles are) -> Oauth2
- In Oauth2 add a redirect like this:   http://127.0.0.1:8000/discord/login/callback/
- Now go to your admin page and in the Social APPLICATIONS section add application
- Add discord app there enter the client key ..... client secret..... and in token add anything you like

** **

## Images
![Screenshot](https://media.discordapp.net/attachments/759043214153089043/760334175043059712/unknown.png)
![SC](https://media.discordapp.net/attachments/759043214153089043/759163204693262377/unknown.png?width=400&height=59)
![sc](https://media.discordapp.net/attachments/759043214153089043/759163230374985798/unknown.png)
##### Please remember to choose the sites in the choose section
![sc](https://cdn.discordapp.com/attachments/759043214153089043/761866434627895296/unknown.png)
##### You should select them and transfer

If you have problems in setting up please post in [#Code-jam-website](https://discordapp.com/channels/501090983539245061/763445637441519646/)
