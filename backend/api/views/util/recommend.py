# 推荐活动的加权计算
import math

from django.db.models import Q
from django.utils import timezone

from api.models import User
from api.models import ActivityUseField
from api.models import UserInGroup
from api.models import UserCreateActivity
from api.models import UserInActivity
from api.models import GroupCreateActivity
from api.models import UserFavor

pog_weight_max = 100
favor_weight_max = 250
scale_weight_max = 100
time_weight_max = 100

pog_weight_origin = -math.log(pog_weight_max)
pog_person_priority, pog_group_priority = 0.8, 1

scale_weight_origin = -math.log(scale_weight_max)
scale_maximum_priority, scale_capacity_priority = 0.65, 0.35

favor_weight_origin = -math.log(favor_weight_max)

# 参照数据集
total_activities = dict()  # 候选活动
person_liveness = dict()  # 用户活跃度
group_liveness = dict()  # 团体活跃度
category_priority = dict()  # 活动类别优先级
joined_activities = set()


# 团体活动优先于个人活动，人数越多的团体优先度越高
def cal_pog_weight(activity):
    if total_activities.get(activity)['type'] == 0:  # 个人
        quantity = person_liveness.get(str(total_activities.get(activity)['creator'].uid))
        res = (-math.exp(-(quantity / 40) - pog_weight_origin) + pog_weight_max) * pog_person_priority
    else:
        quantity = group_liveness.get(str(total_activities.get(activity)['creator'].gid))
        res = (-math.exp(-(quantity / 40) - pog_weight_origin) + pog_weight_max) * pog_group_priority
    return res if res > 0 else 0


# 活动人数规模越大者优先
def cal_scale_weight(activity):
    maximum = total_activities.get(activity)['activity'].maximum
    capacity = total_activities.get(activity)['activity'].capacity
    return (-math.exp(-(maximum / 100) - scale_weight_origin) + scale_weight_max) * scale_maximum_priority + \
        (-math.exp(-(capacity / 100) - scale_weight_origin) + scale_weight_max) * scale_capacity_priority


# 参加过或点赞过的活动类别优先
def cal_favor_weight(activity):
    category = total_activities.get(activity)['activity'].category
    quantity = category_priority.get(category, 0)
    return -math.exp(-(quantity / 30) - favor_weight_origin) + favor_weight_max


# TODO 根据时间习惯评判优先级
def cal_time_weight(activity):
    pass


def initialize(user):
    """ 推荐系统初始化，获取必要数据集 """
    # 获取用户可见的有效活动
    records = ActivityUseField.objects.filter(start_time__gt=timezone.now())
    groups = list(map(lambda param: param.gid, UserInGroup.objects.filter(uid=user)))
    for record in records:
        if record.aid.type == 0:    # 个人
            if not record.aid.private or UserCreateActivity.objects.filter(aid=record.aid, uid=user).first():
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
        if record.uid == user:
            joined_activities.add(record.aid)
            category_priority[record.aid.category] = category_priority.get(record.aid.category, 0) + 1
    # 统计团体活跃度
    for record in GroupCreateActivity.objects.all():
        group_liveness[str(record.gid.gid)] = group_liveness.get(str(record.gid.gid), 0) + 1

    # 统计用户喜欢的活动类型
    for record in UserFavor.objects.filter(uid=user):
        category_priority[record.category] = category_priority.get(record.category, 0) + record.cnt


def get_recommend_activity(uid):
    user = User.objects.get(uid=uid)
    initialize(user)
    activity_weight = []
    for activity in total_activities:
        weight1 = cal_pog_weight(activity)
        print(weight1)
        weight2 = cal_scale_weight(activity)
        print(weight2)
        weight3 = cal_favor_weight(activity)
        print(weight3)
        activity_weight.append((total_activities.get(activity)['activity'], weight1 + weight2 + weight3))

    # 排序取前五个
    sorted_list = sorted(activity_weight, key=lambda x: x[1], reverse=True)
    ret_list, cnt = [], 0
    for element in sorted_list:
        if cnt < 5:
            ret_list.append({
                "aid": element[0].aid,
                "name": element[0].name,
                "category": element[0].category,
                "picture": element[0].picture.url if element[0].picture else None,
                "is_joined": element[0] in joined_activities
            })
            cnt += 1
    return ret_list
