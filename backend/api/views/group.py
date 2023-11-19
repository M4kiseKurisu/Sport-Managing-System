"""
管理团体实体
"""
import json
import random
from django.http import JsonResponse

from api.models import Group
from api.views import user_group


def genid():
    new_id = random.randint(0, 99999999)
    while Group.objects.filter(gid=new_id):
        new_id = random.randint(0, 99999999)
    return new_id


def create(request):
    """ 用户创建团体 """
    if request.method == 'POST':
        data: dict = json.loads(request.body)
        uid = data.get("uid")
        group_name = data.get("group_name")
        group_desc = data.get("group_desc")
        maximum = data.get("maximum")

        if Group.objects.filter(group_name=group_name):
            return JsonResponse({"msg": "团体名称已存在", "status": False, "group_name": None, "gid": None})
        else:
            # 添加团体信息
            gid = genid()
            data.pop('uid')
            new_group = Group(gid=gid, **data)
            new_group.save()
            # 添加用户团体联系
            user_group.add_relation(uid, gid, 0)
            return JsonResponse({"msg": "团体创建成功", "group_name": group_name, "gid": gid})
    else:
        return JsonResponse({"msg": "请求方式有误", "status": False})


def join(request):
    """ 用户申请加入团体 """
    if request.method == 'POST':
        data: dict = json.loads(request.body)
        print(data)
        if user_group.add_apply(data.get("uid"), data.get("gid"), data.get("content")):
            return JsonResponse({"msg": "申请信息已发送", "status": True})
        else:
            return JsonResponse({"msg": "已有申请信息等待审批", "status": False})
    else:
        return JsonResponse({"msg": "请求方式有误"})


def apply(request):
    """ 团体申请相关 """
    if request.method == 'GET':
        uid = request.GET.get('uid')
        is_manager = request.GET.get('is_manager')
        lst = user_group.search_apply(uid, is_manager == "true")
        return JsonResponse({"msg": "请求成功", "list": lst})
    elif request.method == 'POST':
        data: dict = json.loads(request.body)
        print(data)
        if user_group.handle_apply(data.get('mid'), data.get('uid'), data.get('gid'), data.get('res')):
            return JsonResponse({"msg": "处理完成", "status": True})
        else:
            return JsonResponse({"msg": "当前用户无权限处理该团体申请", "status": False})
    else:
        return JsonResponse({"msg": "请求方式有误", "status": False})
