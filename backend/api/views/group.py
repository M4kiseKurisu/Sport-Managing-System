"""
管理团体实体
"""
import json
import random
from django.http import JsonResponse
from django.db.models import Q

from api.models import Group
from api.models import User
from api.views import user_group


def genid():
    new_id = random.randint(0, 99999999)
    while Group.objects.filter(gid=new_id):
        new_id = random.randint(0, 99999999)
    return new_id


def view(request):
    """ 用户查看团体中心综述 """
    if request.method == 'GET':
        key = request.GET.get('keyword') or ''
        uid = request.GET.get('uid')
        groups = Group.objects.filter(Q(group_name__icontains=key) | Q(group_desc__icontains=key))
        joined_groups = list(map(lambda param: param.gid.gid, user_group.search_relation(uid)))

        lst = list(map(lambda param: {"gid": param.gid, "group_name": param.group_name, "group_desc": param.group_desc,
                                      "tag": param.tag, "capacity": param.capacity, "maximum": param.maximum,
                                      "creator": param.creator.user_name, "is_joined": param.gid in joined_groups,
                                      "pic": param.picture.url if param.picture else None},
                       groups))

        return JsonResponse({"msg": "团体信息请求成功", "status": True, "list": lst})

    else:
        return JsonResponse({"msg": "请求方式有误", "status": False})


def detail(request):
    """ 团体具体信息 """
    pass


def create(request):
    """ 用户创建团体 """
    if request.method == 'POST':
        data = request.POST
        print(data)
        uid = data.get("uid")
        group_name = data.get("group_name")
        group_desc = data.get("group_desc")
        maximum = data.get("maximum")
        tag = data.get("tag")

        if Group.objects.filter(group_name=group_name):
            return JsonResponse({"msg": "团体名称已存在", "status": False})
        else:
            # 添加团体信息
            gid = genid()
            creator = User.objects.get(uid=uid)
            new_group = Group(gid=gid, creator=creator, group_name=group_name, group_desc=group_desc,
                              tag=tag, maximum=maximum, capacity=1, picture=request.FILES['picture'])
            new_group.save()
            # 添加用户团体联系
            user_group.add_relation(uid, gid, 0)
            return JsonResponse({"msg": "团体创建成功", "status": True, "group_name": group_name, "gid": gid})
    else:
        return JsonResponse({"msg": "请求方式有误", "status": False})


def join(request):
    """ 用户申请加入团体 """
    if request.method == 'POST':
        data: dict = json.loads(request.body)
        print(data)
        uid = data.get("uid")
        gid = data.get("gid")
        content = data.get("content")

        msg, status = user_group.add_apply(uid, gid, content)
        return JsonResponse({"msg": msg, "status": status})

    else:
        return JsonResponse({"msg": "请求方式有误", "status": False})


def apply(request):
    """ 查看团体申请信息 """
    if request.method == 'GET':
        uid = request.GET.get('uid')
        method = request.GET.get('method')

        lst = user_group.search_apply(uid, True if method == "accept" else False)
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
