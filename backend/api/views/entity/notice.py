"""
通知实体
"""

import json
import random

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.db.models import Q
from api.models import User
from api.models import Notice


def genid():
    new_id = random.randint(0, 99999999)
    while Notice.objects.filter(nid=new_id):
        new_id = random.randint(0, 99999999)
    return new_id


def add_notice_to_uid(uid, text):
    """ 发送系统通知 """
    user = User.objects.get(uid=uid)
    nid = genid()
    new_notice = Notice(nid=nid, text=text, receiver=user)
    new_notice.save()


def add_notice_to_user(user, text):
    """ 发送系统通知 """
    nid = genid()
    new_notice = Notice(nid=nid, text=text, receiver=user)
    new_notice.save()


@require_http_methods(["GET"])
def notice_list(request):
    """ 获取个人通知 """
    uid = request.GET.get('uid')
    user = User.objects.get(uid=uid)
    lst = list(map(lambda param: {"nid": param.nid, "text": param.text,
                                  "time": param.time.strftime("%Y-%m-%d %H:%M:%S")},
                   Notice.objects.filter(receiver=user)))
    return JsonResponse({"msg": '通知获取成功', "status": True, "list": lst})


@require_http_methods(["POST"])
def notice_confirm(request):
    """ 用户确认系统通知 """
    data: dict = json.loads(request.body)
    print(data)
    uid = data.get('uid', None)
    nid = data.get('nid', None)
    if uid:
        user = User.objects.get(uid=uid)
        Notice.objects.filter(receiver=user).delete()
        return JsonResponse({"msg": '消息确认成功', "status": True})
    elif nid:
        Notice.objects.get(nid=nid).delete()
        return JsonResponse({"msg": '消息确认成功', "status": True})
    else:
        return JsonResponse({"msg": '请确认参数是否正确', "status": False})
