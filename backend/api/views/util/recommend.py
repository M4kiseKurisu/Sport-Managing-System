# 推荐活动的加权计算
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

person_priority, group_priority = 0.35, 0.65


# 团体活动优先于个人活动，人数越多的团体优先度越高
def cal_pog_weight(activity):


def initialize(user):
    """ 推荐系统初始化，获取必要数据集 """
    # 获取必要
    records = ActivityUseField.objects.filter(start_time__gt=timezone.now()).order_by('start_time')
    groups = list(map(lambda param: param.gid, UserInGroup.objects.filter(uid=user)))


def cal_weight(user):
    activity_type = activity.type
    weight1 = cal_pog_weight(activity)
