"""
用户和活动联系
"""
from django.db.models import Q

from api.models import User
from api.models import Activity
from api.models import UserInActivity
from api.models import UserCreateActivity
from api.models import GroupCreateActivity
from api.views.entity import notice

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
        rec = UserInActivity(uid=user, aid=activity, like=False)
        rec.save()
        return True


def delete_relation(uid, aid):
    """
     删除用户参与活动记录
     活动创建者则删除活动
    """
    user = User.objects.get(uid=uid)
    activity = Activity.objects.get(aid=aid)
    if activity.type == 0:  # 个人活动
        rec = UserCreateActivity.objects.filter(uid=user, aid=activity)
    else:  # 团体活动
        rec = GroupCreateActivity.objects.filter(uid=user, aid=activity)

    if rec.exists():
        # 撤销活动
        for rec in UserInActivity.objects.filter(aid=activity):
            notice.add_notice_to_user(rec.uid, "您参加的活动 (" + activity.name + ") 已被取消")
        activity.delete()
    else:
        # 删除用户参与活动记录
        UserInActivity.objects.get(uid=user, aid=activity).delete()
        activity.capacity -= 1
        activity.save()
