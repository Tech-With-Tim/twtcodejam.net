from typing import Callable
import requests
import json

from our_secrets import TOKEN
from .cache import TimedCache


class Discord:
    ROOT = "https://discord.com/api/"

    methods = {
        "GET": requests.get,
        "PUT": requests.put,
        "POST": requests.post,
        "DELETE": requests.delete
    }

    def __init__(self, *, token: str):

        self.headers = {
            'Authorization': f'Bot {token}'
        }

    def __request(self, retry: Callable[[int], object], method: str = "GET", url: str = "", data: dict = None) -> dict:
        if data is not None:
            if isinstance(data, dict):
                data = json.dumps(data)

        print(f"{method} @ {retry.__name__}")

        try:
            return self.methods[method](url=f"{self.ROOT}{url}", json=data, headers=self.headers).json()
        except Exception as e:
            raise e

    def get_guild(self, guild_id: int = 501090983539245061):
        return self.__request(retry=self.get_guild, url="guilds/{}".format(guild_id))

    def get_member(self, member_id: int, guild_id: int = 501090983539245061):
        return self.__request(retry=self.get_member, url="guilds/{g}/members/{m}".format(g=guild_id, m=member_id))

    def get_roles(self, guild_id: int = 501090983539245061):
        return self.__request(retry=self.get_roles, url="guilds/{}/roles".format(guild_id))


client = Discord(token=TOKEN)
HELPER_ID: int = 541272748161499147
MOD_ID: int = 511332506780434438
ADMIN_ID: int = 580911082290282506
TIM_ID: int = 511334601977888798
ALL_ROLES = {
    "TIM": TIM_ID,
    "ADMIN": ADMIN_ID,
    "MOD": MOD_ID,
    "HELPER": HELPER_ID
}


__cache = TimedCache(seconds=10)


def get_member(member_id: int) -> dict:
    member = __cache.get(member_id)
    if member is None:
        __cache[member_id] = member = client.get_member(member_id=member_id)
    return member


def is_helper(member_id: int) -> bool:
    member = get_member(member_id=member_id)
    return str(HELPER_ID) in member["roles"]


def is_mod(member_id: int) -> bool:
    member = get_member(member_id=member_id)
    return str(MOD_ID) in member["roles"]


def is_admin(member_id: int) -> bool:
    member = get_member(member_id=member_id)
    return str(ADMIN_ID) in member["roles"]


def is_tim(member_id: int) -> bool:
    member = get_member(member_id=member_id)
    return str(TIM_ID) in member["roles"]


def is_any(*roles, member_id: int) -> bool:
    member = get_member(member_id=member_id)
    return any(str(ALL_ROLES[role]) in member["roles"] for role in roles)


def is_staff(member_id: int) -> bool:
    return is_any("HELPER", "MOD", "ADMIN", "TIM", member_id=member_id)
