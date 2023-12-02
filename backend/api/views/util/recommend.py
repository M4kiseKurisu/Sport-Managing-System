# 推荐活动的加权计算
import math

from django.db.models import Q
from django.utils import timezone

from api.models import User
from api.models import Activity
from api.models import ActivityUseField
from api.models import UserInGroup
from api.models import UserCreateActivity
from api.models import UserInActivity
from api.models import GroupCreateActivity
from api.views.relation import user_activity
from api.views.relation import user_group
from api.views.relation import group_activity
from api.views.relation import activity_field

pog_weight_max = 100
favor_weight_max = 250
scale_weight_max = 100
time_weight_max = 100

person_priority, group_priority = 0.8, 1
pog_weight_origin = -math.log(pog_weight_max)

# 参照数据集
total_activities = dict()  # 候选活动
person_liveness = dict()  # 用户活跃度
group_liveness = dict()  # 团体活跃度


# 团体活动优先于个人活动，人数越多的团体优先度越高
def cal_pog_weight(activity):
    if total_activities.get(activity)['type'] == 0:  # 个人
        quantity = person_liveness.get(str(total_activities.get(activity)['creator'].uid))
        res = (-math.exp(-(quantity / 40) - pog_weight_origin) + pog_weight_max) * person_priority
    else:
        quantity = group_liveness.get(str(total_activities.get(activity)['creator'].gid))
        res = (-math.exp(-(quantity / 40) - pog_weight_origin) + pog_weight_max) * group_priority
    return res if res > 0 else 0



def initialize(user):
    """ 推荐系统初始化，获取必要数据集 """
    # 获取用户可见的有效活动
    records = ActivityUseField.objects.filter(start_time__gt=timezone.now()).order_by('start_time')
    groups = list(map(lambda param: param.gid, UserInGroup.objects.filter(uid=user)))
    for record in records:
        if record.aid.type == 0 and not record.aid.private:  # 个人
            total_activities[str(record.aid.aid)] = {"type": 0, "activity": record.aid, "time": record.start_time}
        elif record.aid.type == 1:  # 团体
            if not record.aid.private:
                total_activities[str(record.aid.aid)] = {"type": 1, "activity": record.aid, "time": record.start_time}
            elif GroupCreateActivity.objects.filter(aid=record.aid, gid__in=groups):
                total_activities[str(record.aid.aid)] = {"type": 1, "activity": record.aid, "time": record.start_time}

    # 填入活动创建者信息
    for record in UserCreateActivity.objects.all():
        if str(record.aid.aid) in total_activities:
            total_activities.get(str(record.aid.aid))["creator"] = record.uid
    for record in GroupCreateActivity.objects.all():
        if str(record.aid.aid) in total_activities:
            total_activities.get(str(record.aid.aid))["creator"] = record.gid

    # 统计个人活跃度
    for record in UserInActivity.objects.all():
        person_liveness[str(record.uid.uid)] = person_liveness.get(str(record.uid.uid), 0) + 1
    # 统计团体活跃度
    for record in GroupCreateActivity.objects.all():
        group_liveness[str(record.gid.gid)] = group_liveness.get(str(record.gid.gid), 0) + 1


def cal_weight(uid):
    user = User.objects.get(uid=uid)
    initialize(user)
    for activity in total_activities:
        weight1 = cal_pog_weight(activity)
