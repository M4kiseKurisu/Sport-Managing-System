"""
团体实体
"""
import json
import random

from django.http import JsonResponse
from django.db.models import Q
from django.views.decorators.http import require_http_methods

from api.models import Group
from api.models import User
from api.views.relation import user_group


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
        joined_groups = list(map(lambda param: param.gid.gid, user_group.search_relation(uid, None)))

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
                              tag=tag, maximum=maximum, capacity=0, picture=request.FILES['picture'])
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


@require_http_methods(["GET", "POST"])
def apply(request):
    if request.method == 'GET':
        """ 查看团体申请信息 """
        uid = request.GET.get('uid')
        method = request.GET.get('method')
        lst = []

        if method == "accept":
            applies = user_group.search_accept_apply(uid)
            for a in applies:
                print(a.apply_time)
                temp = {"uid": a.uid.uid, "user_name": a.uid.user_name, "content": a.content,
                        "gid": a.gid.gid, "group_name": a.gid.group_name,
                        "time": a.apply_time.strftime("%Y-%m-%d %H:%M:%S"),
                        "status": a.get_status_display()}
                lst.append(temp)

        elif method == "send":
            applies = user_group.search_send_apply(uid)
            for a in applies:
                temp = {"gid": a.gid.gid, "group_name": a.gid.group_name, "content": a.content,
                        "time": a.apply_time.strftime("%Y-%m-%d %H:%M:%S"),
                        "status": a.get_status_display()}
                lst.append(temp)
        else:
            return JsonResponse({"msg": "method参数错误", "status": False})

        return JsonResponse({"msg": "团体申请获取成功", "status": True, "list": lst})

    elif request.method == 'POST':
        """ 处理团体申请 """
        data: dict = json.loads(request.body)
        print(data)
        if user_group.handle_apply(data.get('uid'), data.get('gid'), data.get('res')):
            return JsonResponse({"msg": "处理完成", "status": True})
        else:
            return JsonResponse({"msg": "团体人数已达上限", "status": False})


@require_http_methods(["POST"])
def exit_out(request):
    """ 用户退出团体 """
    data: dict = json.loads(request.body)
    print(data)
    uid = data.get('uid')
    gid = data.get('gid')
    user_group.delete_relation(uid, gid)
    return JsonResponse({"msg": "团体已退出", "status": True})


@require_http_methods(["GET"])
def members_list(request):
    """ 查看团体成员列表 """
    gid = request.GET.get('gid')
    keyword = request.GET.get('keyword', '')
    members = user_group.search_relation(None, gid)
    members = list(map(lambda param: {"uid": param.uid.uid, "user_name": param.uid.user_name,
                                      "pic": param.uid.picture.url if param.uid.picture else None,
                                      "type": param.get_type_display()},
                       members.filter(uid__user_name__icontains=keyword).order_by('type')))
    return JsonResponse({"msg": "成员列表获取成功", "status": True, "list": members})


@require_http_methods(["POST"])
def members_remove(request):
    """ 移除团体成员 """
    data: dict = json.loads(request.body)
    uid = data.get('uid')
    gid = data.get('gid')
    user_group.delete_relation(uid, gid)
    return JsonResponse({"msg": "成员已移除", "status": True})


@require_http_methods(["POST"])
def members_authority(request):
    data: dict = json.loads(request.body)
    uid = data.get('uid')
    gid = data.get('gid')
    member_type = data.get('type')
    if member_type == 0:
        return JsonResponse({"msg": "无法修改团体创建人信息", "status": False})
    elif member_type == 1:
        user_group.modify_relation(uid, gid, member_type)
        return JsonResponse({"msg": "添加团体管理员成功", "status": True})
    elif member_type == 2:
        user_group.modify_relation(uid, gid, member_type)
        return JsonResponse({"msg": "移除团体管理员成功", "status": True})
