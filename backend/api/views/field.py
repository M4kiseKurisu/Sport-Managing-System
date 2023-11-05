"""
管理运动场地实体
"""
import json
import random
from django.http import JsonResponse

from api.models import Field


def genid():
    new_id = random.randint(0, 99999999)
    while Field.objects.filter(fid=new_id):
        new_id = random.randint(0, 99999999)
    return new_id


def add(request):
    """ 新增场地 """
    if request.method == 'POST':
        data: dict = json.loads(request.body)
        new_field = Field(fid=genid(), **data)
        new_field.save()
        return JsonResponse({"msg": "场地信息添加成功"})
    else:
        return JsonResponse({"msg": "请求方式有误"})


def search(request):
    """ 查询场地信息 """
    if request.method == 'GET':
        category = request.GET.get('category')
        if category:
            lst = list(
                map(lambda param: {'fid': param.fid, 'location': param.location, "open_time": param.open_time,
                                   "close_time": param.close_time},
                    Field.objects.filter(category=category))
            )
            return JsonResponse({"msg": "场地信息请求成功", "list": lst})
        else:
            lst = list(map(lambda param: param.get('category'), Field.objects.values('category').all().distinct()))
        return JsonResponse({"msg": "场地信息请求成功", "list": lst})
    else:
        return JsonResponse({"msg": "请求方式有误"})
