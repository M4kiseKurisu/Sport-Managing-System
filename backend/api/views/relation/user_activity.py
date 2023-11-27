"""
用户和活动联系
"""
from django.db.models import Q

from api.models import User
from api.models import Activity
from api.models import UserInActivity
from api.models import UserCreateActivity


def add_create_relation(uid, aid):
    """ 增加用户创建活动记录 """
    user = User.objects.get(uid=uid)
    activity = Activity.objects.get(aid=aid)
    rec = UserCreateActivity(uid=user, aid=activity)
    rec.save()


def add_relation(uid, aid):
    """ 增加用户参与活动记录 """
    user = User.objects.get(uid=uid)
    activity = Activity.objects.get(aid=aid)
    if activity.maximum == activity.capacity:
        return False
    else:
        # 增加活动参与人数
        activity.capacity += 1
        activity.save()
        # 增加用户参与记录
        rec = UserInActivity(uid=user, aid=activity)
        rec.save()
        return True
