from allauth.socialaccount.models import SocialAccount
from django.core.handlers.wsgi import WSGIRequest

from TWT import discord
from random import randint

def get_discord_context(request: WSGIRequest) -> dict:
    context = {}

    try:
        user = SocialAccount.objects.get(user_id=request.user.id)
    except SocialAccount.DoesNotExist:
        pass
    else:
        context["user_id"] = user.uid
        #context["avatar_url"] = user.get_avatar_url()
        context['discord_user'] = user
        avatar_url = user.get_avatar_url()
        if avatar_url.endswith("None.png"):
            random = randint(0,4)
            avatar_url = f'https://cdn.discordapp.com/embed/avatars/{random}.png'

        context["avatar_url"] = avatar_url
        context["username"] = user.extra_data["username"]
        context["discriminator"] = user.extra_data["discriminator"]
        context["is_verified"] = discord.is_verified(member_id=user.uid)
        context["is_admin"] = is_admin = discord.is_admin(member_id=user.uid)
        if not is_admin:
            context["is_mod"] = is_mod = discord.is_mod(member_id=user.uid)
            context["is_challenge_host"] = discord.is_challenge_host(member_id=user.uid)
            if not is_mod:
                context["is_helper"] = discord.is_helper(member_id=user.uid)
            else:
                context["is_helper"] = True
        else:
            context["is_mod"] = True
            context["is_helper"] = True
            context["is_challenge_host"] = True

        if any((context["is_admin"], context["is_mod"], context["is_helper"])):
            context["is_staff"] = True
            context["is_verified"] = True
        else:
            context["is_staff"] = False

    finally:
        try:
            is_verified = context["is_verified"]
        except KeyError:
            context["is_verified"] = False
        return context
