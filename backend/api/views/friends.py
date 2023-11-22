"""
好友联系
"""

from django.db.models import Q

from api.models import User
from api.models import Friend


def search_relation(uid):
    """ 查询用户的好友 """
    lst = []
    user = User.objects.filter(uid=uid).first()
    if user:
        lst += list(map(lambda param: param.uid2, Friend.objects.filter(uid1=user)))
        lst += list(map(lambda param: param.uid1, Friend.objects.filter(uid2=user)))
        return lst
    else:
        return None
