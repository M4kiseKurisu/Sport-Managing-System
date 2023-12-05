"""
团体和活动联系
"""
from api.models import User
from api.models import Group
from api.models import Activity
from api.models import GroupCreateActivity


def add_create_relation(uid, gid, aid):
    """ 增加用户创建活动记录 """
    user = User.objects.get(uid=uid)
    group = Group.objects.get(gid=gid)
    activity = Activity.objects.get(aid=aid)
    rec = GroupCreateActivity(uid=user, gid=group, aid=activity)
    rec.save()