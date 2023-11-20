"""
器材实体
"""
import json
import random
from datetime import datetime

from django.http import JsonResponse

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
        new_equipment = Equipment(eid=genid(), category=request.POST.get('category'),
                                  amount=request.POST.get('amount'), picture=request.FILES['picture'])
        new_equipment.save()
        return JsonResponse({"msg": "器材信息添加成功", "status": True})
    else:
        return JsonResponse({"msg": "请求方式有误", "status": False})


def view(request):
    """ 查看器材信息 """
    if request.method == 'GET':
        key = request.GET.get('keyword')
        if key:
            lst = list(map(lambda param: {"eid": param.eid, "category": param.category, "amount": param.amount,
                                          "pic": param.picture.url},
                           Equipment.objects.filter(category__icontains=key)))
        else:
            lst = list(map(lambda param: {"eid": param.eid, "category": param.category,
                                          "amount": param.amount, "pic": param.picture.url},
                           Equipment.objects.all()))

        return JsonResponse({"msg": "器材信息请求成功", "status": True, "list": lst})

    else:
        return JsonResponse({"msg": "请求方式有误", "status": False})


def borrow(request):
    """ 借用器材 """
    if request.method == 'POST':
        data: dict = json.loads(request.body)
        print(data)
        equipment = Equipment.objects.get(category=data.get("category"))
        start_time = datetime.strptime(data.get("start_time"), "%Y-%m-%d %H:%M:%S")
        end_time = datetime.strptime(data.get("end_time"), "%Y-%m-%d %H:%M:%S")

        if data.get("amount") > equipment.amount:
            return JsonResponse({"msg": "器材剩余数量不足", "status": False})

        if data.get("uid"):  # 用户借用
            user = User.objects.get(uid=data.get("uid"))
            if UserEquipment.objects.filter(eid=equipment, uid=user, start_time=start_time, end_time=end_time).first():
                return JsonResponse({"msg": "同一时间段内已经存在同类借用记录", "status": False})

            new_record = UserEquipment(eid=equipment, uid=user, lend_amount=data.get("amount"),
                                       start_time=start_time, end_time=end_time)
            new_record.save()
        else:  # 团体借用
            group = Group.objects.get(gid=data.get("gid"))
            if GroupEquipment.objects.filter(eid=equipment, gid=group, start_time=start_time,
                                             end_time=end_time).first():
                return JsonResponse({"msg": "同一时间段内已经存在同类借用记录", "status": False})

            new_record = GroupEquipment(eid=equipment, gid=group, lend_amount=data.get("amount"),
                                        start_time=start_time, end_time=end_time)
            new_record.save()

        equipment.amount -= data.get("amount")
        equipment.save()

        return JsonResponse({"msg": "器材借用成功", "status": True})

    else:
        return JsonResponse({"msg": "请求方式有误", "status": False})


def record(request):
    """ 查看器材借用记录 """
    if request.method == 'GET':
        uid = request.GET.get("uid")
        gid = request.GET.get("gid")

        if uid:
            user = User.objects.get(uid=uid)
            lst = list(map(
                lambda param: {"pic": param.eid.picture.url,
                               "category": param.eid.category, "lend_amount": param.lend_amount,
                               "start_time": param.start_time.strftime("%Y-%m-%d %H:%M:%S"),
                               "end_time": param.end_time.strftime("%Y-%m-%d %H:%M:%S"),
                               "is_return": param.get_is_return_display()},
                UserEquipment.objects.filter(uid=user).order_by('-end_time')
            ))
        else:
            group = Group.objects.get(gid=gid)
            lst = list(map(
                lambda param: {"pic": param.eid.picture.url,
                               "category": param.eid.category, "lend_amount": param.lend_amount,
                               "start_time": param.start_time.strftime("%Y-%m-%d %H:%M:%S"),
                               "end_time": param.end_time.strftime("%Y-%m-%d %H:%M:%S"),
                               "is_return": param.get_is_return_display()},
                GroupEquipment.objects.filter(gid=group).order_by('-end_time')
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
        start_time = datetime.strptime(data.get("start_time"), "%Y-%m-%d %H:%M:%S")
        end_time = datetime.strptime(data.get("end_time"), "%Y-%m-%d %H:%M:%S")
        equipment = Equipment.objects.get(eid=data.get("eid"))

        if uid:  # 用户借用
            user = User.objects.get(uid=uid)
            borrow_record = UserEquipment.objects.filter(
                eid=equipment, uid=user, start_time=start_time, end_time=end_time).first()
        else:  # 团体借用
            group = Group.objects.get(gid=gid)
            borrow_record = GroupEquipment.objects.filter(
                eid=equipment, gid=group, start_time=start_time, end_time=end_time).first()

        if borrow_record:
            equipment.amount += borrow_record.lend_amount
            equipment.save()
            borrow_record.is_return = 2
            borrow_record.save()
            return JsonResponse({"msg": "器材归还成功", "status": True})
        else:
            return JsonResponse({"msg": "不存在借用记录", "status": False})

    else:
        return JsonResponse({"msg": "请求方式有误", "status": False})
