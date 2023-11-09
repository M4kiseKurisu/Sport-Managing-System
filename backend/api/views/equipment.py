"""
器材实体
"""
import json
import random
from django.http import JsonResponse

from api.models import Equipment


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
