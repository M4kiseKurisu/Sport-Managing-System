"""
器材实体
"""
import json
import random
from datetime import datetime, timedelta

from django.http import JsonResponse
from django.utils import timezone

from api.models import Equipment
from api.models import User
from api.models import Group
from api.models import GroupEquipment
from api.models import UserEquipment


def genid():
    new_id = random.randint(0, 99999999)
    while Equipment.objects.filter(eid=new_id):
        new_id = random.randint(0, 99999999)
    return new_id


def add(request):
    """ 增加器材 """
    if request.method == 'POST':
        data: dict = json.loads(request.body)
        new_equipment = Equipment(eid=genid(), **data)
        new_equipment.save()
        return JsonResponse({"msg": "场地信息添加成功"})
    else:
        return JsonResponse({"msg": "请求方式有误"})


def view(request):
    """ 查看器材信息 """
    if request.method == 'GET':
        category = request.GET.get('category')
        if category:
            equipment = Equipment.objects.filter(category=category).first()
            return JsonResponse(
                {"msg": "器材信息请求成功", "eid": equipment.eid, "category": category, "amount": equipment.amount}
            ) if equipment else JsonResponse({"msg": "不存在这种类别的器材"})

        else:
            lst = list(map(lambda param: param.get('category'), Equipment.objects.values('category').all().distinct()))
        return JsonResponse({"msg": "器材信息请求成功", "list": lst})

    else:
        return JsonResponse({"msg": "请求方式有误"})


def borrow(request):
    """ 借用器材 """
    if request.method == 'POST':
        data: dict = json.loads(request.body)
        print(data)
        equipment = Equipment.objects.get(category=data.get("category"))
        if data.get("amount") > equipment.amount:
            return JsonResponse({"msg": "借用器材数量过多", "status": False})
        else:
            equipment.amount -= data.get("amount")
            equipment.save()

        if data.get("uid"):  # 用户借用
            user = User.objects.get(uid=data.get("uid"))
            new_record = UserEquipment(eid=equipment, uid=user, lend_amount=data.get("amount"))
            new_record.save()
        else:  # 团体借用
            group = Group.objects.get(gid=data.get("gid"))
            new_record = GroupEquipment(eid=equipment, gid=group, lend_amount=data.get("amount"))
            new_record.save()

        return JsonResponse({"msg": "器材借用成功", "status": True})

    else:
        return JsonResponse({"msg": "请求方式有误", "status": False})


def record(request):
    """ 查看器材借用记录 """
    if request.method == 'GET':
        uid = request.GET.get("uid")
        gid = request.GET.get("gid")
        lst = []

        if uid:
            user = User.objects.get(uid=uid)
            lst = list(map(
                lambda param: {"time": param.lend_time.strftime("%Y-%m-%d %H:%M:%S"), "eid": param.eid.eid,
                               "lend_amount": param.lend_amount, "is_return": param.is_return},
                UserEquipment.objects.filter(uid=user)
            ))
        else:
            group = Group.objects.get(gid=gid)
            lst = list(map(
                lambda param: {"time": param.lend_time.strftime("%Y-%m-%d %H:%M:%S"), "eid": param.eid.eid,
                               "lend_amount": param.lend_amount, "is_return": param.is_return},
                GroupEquipment.objects.filter(gid=group)
            ))
        return JsonResponse({"msg": "器材信息请求成功", "status": True, "list": lst})

    else:
        return JsonResponse({"msg": "请求方式有误", "status": False})


def give_back(request):
    """ 归还器材 """
    if request.method == 'POST':
        data: dict = json.loads(request.body)
        uid = data.get("uid")
        gid = data.get("gid")
        lend_time = datetime.strptime(data.get("time"), "%Y-%m-%d %H:%M:%S")
        lend_next_time = lend_time + timedelta(seconds=1)
        equipment = Equipment.objects.get(eid=data.get("eid"))

        if uid:  # 用户借用
            user = User.objects.get(uid=uid)
            borrow_record = UserEquipment.objects.filter(
                eid=equipment, uid=user, lend_time__range=(lend_time, lend_next_time), is_return=False).first()
        else:  # 团体借用
            group = Group.objects.get(gid=gid)
            borrow_record = GroupEquipment.objects.filter(
                eid=equipment, gid=group, lend_time__range=(lend_time, lend_next_time), is_return=False).first()

        if borrow_record:
            equipment.amount += borrow_record.lend_amount
            equipment.save()
            borrow_record.is_return = True
            borrow_record.save()
            return JsonResponse({"msg": "器材归还成功", "status": True})
        else:
            return JsonResponse({"msg": "不存在借用记录", "status": False})

    else:
        return JsonResponse({"msg": "请求方式有误", "status": False})
