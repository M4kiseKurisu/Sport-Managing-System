"""
管理运动场地实体
"""
import json
import random

from django.utils.dateparse import parse_date
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from api.models import Field
from api.models import ActivityUseField


def genid():
    new_id = random.randint(0, 99999999)
    while Field.objects.filter(fid=new_id):
        new_id = random.randint(0, 99999999)
    return new_id


@require_http_methods(["POST"])
def add(request):
    """ 新增场地 """
    if request.method == 'POST':
        data: dict = json.loads(request.body)
        new_field = Field(fid=genid(), **data)
        new_field.save()
        return JsonResponse({"msg": "场地信息添加成功", "status": True})


@require_http_methods(["GET"])
def view(request):
    """ 查询场地信息 """
    category = request.GET.get('category')
    if category:
        lst = list(
            map(lambda param: {'fid': param.fid, 'location': param.location, "open_time": param.open_time,
                               "close_time": param.close_time},
                Field.objects.filter(category=category))
        )
        return JsonResponse({"msg": "场地信息请求成功", "status": True, "list": lst})
    else:
        lst = list(map(lambda param: param.get('category'), Field.objects.values('category').all().distinct()))
    return JsonResponse({"msg": "场地信息请求成功", "status": True, "list": lst})


@require_http_methods(["GET"])
def usage(request):
    """ 查看场地使用情况 """
    field = Field.objects.get(fid=request.GET.get('fid'))
    time = parse_date(request.GET.get('time'))
    lst = list(map(lambda param: {"start": param.start_time.strftime("%H:%M:%S"),
                                  "end": param.end_time.strftime("%H:%M:%S")},
                   ActivityUseField.objects.filter(fid=field, start_time__date=time)))
    return JsonResponse({"msg": "场地使用情况获取成功", "status": True, "list": lst})
