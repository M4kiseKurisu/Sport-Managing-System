"""
活动实体
"""
import json
import random

from django.http import JsonResponse
from django.db.models import Q
from django.views.decorators.http import require_http_methods

from api.models import Activity
from api.models import User
from api.views.relation import user_activity
from api.views.relation import group_activity
from api.views.relation import activity_field


def genid():
    new_id = random.randint(0, 99999999)
    while Activity.objects.filter(aid=new_id):
        new_id = random.randint(0, 99999999)
    return new_id


@require_http_methods(["POST"])
def create(request):
    data = request.POST
    print(data)
    # 检查场地是否被占用
    if not activity_field.check_relation(data.get('fid'), data.get('start_time'), data.get('end_time')):
        return JsonResponse({"msg": "当前时段场地不开放或已被占用", "status": False})
    else:
        activity = Activity(aid=genid(), type=data.get('type'), name=data.get('name'), desc=data.get('desc'),
                            category=data.get('category'), tags=data.get('tags'), maximum=data.get('maximum'),
                            capacity=0, favor=0, private=data.get('private') is 'true',
                            picture=request.FILES['picture'])
        activity.save()
        # 添加场地使用记录
        activity_field.add_relation(activity.aid, data.get('fid'), data.get('start_time'), data.get('end_time'))

        # 添加创建信息
        if data.get('type') == '0':  # 个人
            user_activity.add_create_relation(data.get('uid'), activity.aid)
        elif data.get('type') == '1':  # 团体
            group_activity.add_create_relation(data.get('uid'), data.get('gid'), activity.aid)
        else:
            return JsonResponse({"msg": "type参数取值有误", "status": False})

        # 项目创建人参与项目
        user_activity.add_relation(data.get('uid'), activity.aid)
        return JsonResponse({"msg": "活动创建成功", "status": True})


@require_http_methods(["GET"])
def detail(request):
    activity = Activity.objects.get(aid=request.GET.get('aid'))
    data = {
        ""
    }
    return JsonResponse({"msg": "活动详细信息获取成功", "status": True, "data": data})
