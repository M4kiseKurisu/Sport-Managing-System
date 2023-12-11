"""
活动实体
"""
import json
import random

from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.utils.dateparse import parse_date
from django.utils import timezone

from api.models import User
from api.models import Activity
from api.models import UserInActivity
from api.models import ActivityUseField
from api.models import UserCreateActivity
from api.models import GroupCreateActivity
from api.models import UserFavor
from api.views.relation import user_activity
from api.views.relation import user_group
from api.views.relation import group_activity
from api.views.relation import activity_field
from api.views.util import recommend as rcd


def genid():
    new_id = random.randint(0, 99999999)
    while Activity.objects.filter(aid=new_id):
        new_id = random.randint(0, 99999999)
    return new_id


@require_http_methods(["POST"])
def create(request):
    """ 创建新的活动 """
    data = request.POST
    print(data)
    if int(data.get('maximum')) < 1:
        return JsonResponse({"msg": "活动人数至少为1", "status": False})
    # 检查场地是否被占用
    elif not activity_field.check_relation(data.get('fid'), data.get('start_time'), data.get('end_time')):
        return JsonResponse({"msg": "当前时段场地不开放或已被占用", "status": False})
    else:
        activity = Activity(aid=genid(), type=data.get('type'), name=data.get('name'), desc=data.get('desc'),
                            category=data.get('category'), tags=data.get('tags'), maximum=data.get('maximum'),
                            capacity=0, favor=0, private=data.get('private') == 'true',
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
def active(request):
    """ 查看当前可见的有效活动 """
    uid = request.GET.get('uid')
    time = request.GET.get('time', '')
    text = request.GET.get('text', '')
    category = request.GET.get('category', '')
    tag = request.GET.get('tag', '')
    activity_type = int(request.GET.get('type'))

    query = Q(start_time__gt=timezone.now())
    if time:
        query &= Q(start_time__date=parse_date(time))
    if text:
        query &= Q(Q(aid__name__icontains=text) | Q(aid__desc__icontains=text))
    if category:
        query &= Q(aid__category__icontains=category)
    if tag:
        query &= Q(aid__tags__icontains=tag)
    if activity_type != 2:
        query &= Q(aid__type__icontains=activity_type)
    records = ActivityUseField.objects.filter(query).order_by('start_time')
    lst = []
    groups = list(map(lambda param: param.gid, user_group.search_relation(uid, None)))
    actives = list((map(lambda param: param.aid, UserInActivity.objects.filter(uid=uid))))
    for record in records:
        flag = False
        if record.aid.type == 0:  # 个人
            if not record.aid.private:
                flag = True
            elif UserCreateActivity.objects.filter(aid=record.aid, uid=uid):
                flag = True
        elif record.aid.type == 1:  # 团体
            if not record.aid.private:
                flag = True
            elif GroupCreateActivity.objects.filter(aid=record.aid, gid__in=groups):
                flag = True

        if flag:
            lst.append({
                "aid": record.aid.aid,
                "name": record.aid.name,
                "type": record.aid.get_type_display(),
                "category": record.aid.category,
                "capacity": record.aid.capacity,
                "maximum": record.aid.maximum,
                "start_time": record.start_time.strftime("%Y-%m-%d %H:%M:%S"),
                "end_time": record.end_time.strftime("%Y-%m-%d %H:%M:%S"),
                "picture": record.aid.picture.url if record.aid.picture else None,
                "is_joined": record.aid in actives
            })

    return JsonResponse({"msg": "活动信息获取成功", "status": True, "list": lst})


@require_http_methods(["GET"])
def inactive(request):
    """ 查看当前可见的结束的活动 """
    uid = request.GET.get('uid')
    time = request.GET.get('time', '')
    text = request.GET.get('text', '')
    category = request.GET.get('category', '')
    activity_type = int(request.GET.get('type'))
    method = request.GET.get('method')

    query = Q(end_time__lt=timezone.now())
    if time:
        query &= Q(start_time__date=parse_date(time))
    if text:
        query &= Q(Q(aid__name__icontains=text) | Q(aid__desc__icontains=text))
    if category:
        query &= Q(aid__category__icontains=category)
    if activity_type != 2:
        query &= Q(aid__type__icontains=activity_type)

    if method == "time":
        records = ActivityUseField.objects.filter(query).order_by('-start_time')
    elif method == "favor":
        records = ActivityUseField.objects.filter(query).order_by('-aid__favor')
    elif method == "scale":
        records = ActivityUseField.objects.filter(query).order_by('-aid__maximum')
    else:
        return JsonResponse({"msg": "method参数有误", "status": False})

    lst = []
    groups = list(map(lambda param: param.gid, user_group.search_relation(uid, None)))
    actives = list((map(lambda param: param.aid, UserInActivity.objects.filter(uid=uid))))
    for record in records:
        flag = False
        if record.aid.type == 0 and not record.aid.private:  # 个人
            flag = True
        elif record.aid.type == 1:  # 团体
            if not record.aid.private:
                flag = True
            elif GroupCreateActivity.objects.filter(aid=record.aid, gid__in=groups):
                flag = True

        if flag:
            lst.append({
                "aid": record.aid.aid,
                "name": record.aid.name,
                "type": record.aid.get_type_display(),
                "category": record.aid.category,
                "capacity": record.aid.capacity,
                "maximum": record.aid.maximum,
                "start_time": record.start_time.strftime("%Y-%m-%d %H:%M:%S"),
                "end_time": record.end_time.strftime("%Y-%m-%d %H:%M:%S"),
                "picture": record.aid.picture.url if record.aid.picture else None,
                "favor": record.aid.favor,
                "is_joined": record.aid in actives
            })

    return JsonResponse({"msg": "活动信息获取成功", "status": True, "list": lst})


@require_http_methods(["GET"])
def detail(request):
    """ 查看活动的详细信息 """
    activity = Activity.objects.get(aid=request.GET.get('aid'))
    field_usage = ActivityUseField.objects.get(aid=activity)
    participants = list(
        map(lambda param: {"picture": param.uid.picture.url if param.uid.picture else None,
                           "uid": param.uid.uid, "user_name": param.uid.user_name,
                           "gender": param.uid.user_gender},
            UserInActivity.objects.filter(aid=activity))
    )
    data = {
        "aid": activity.aid,
        "type": activity.get_type_display(),
        "activity_name": activity.name,
        "desc": activity.desc,
        "category": activity.category,
        "tags": activity.tags.split('-'),
        "capacity": activity.capacity,
        "maximum": activity.maximum,
        "picture": activity.picture.url if activity.picture else None,
        "start_time": field_usage.start_time.strftime("%Y-%m-%d %H:%M:%S"),
        "end_time": field_usage.end_time.strftime("%Y-%m-%d %H:%M:%S"),
        "location": field_usage.fid.location,
        "favors": activity.favor,
        "participants": participants,
    }

    if activity.type == 0:  # 个人
        creation = UserCreateActivity.objects.get(aid=activity)
        data['uid'] = creation.uid.uid
        data['user_name'] = creation.uid.user_name
    else:  # 团体
        creation = GroupCreateActivity.objects.get(aid=activity)
        data['uid'] = creation.uid.uid
        data['user_name'] = creation.uid.user_name
        data['gid'] = creation.gid.gid
        data['group_name'] = creation.gid.group_name

    return JsonResponse({"msg": "活动详细信息获取成功", "status": True, "data": data})


@require_http_methods(["POST"])
def join(request):
    """ 用户加入活动 """
    data: dict = json.loads(request.body)
    uid = data.get('uid')
    aid = data.get('aid')
    if user_activity.add_relation(uid, aid):
        return JsonResponse({"msg": "成功加入活动", "status": True})
    else:
        return JsonResponse({"msg": "人数已达上限", "status": False})


@require_http_methods(["POST"])
def exit_out(request):
    """ 用户退出、撤销活动 """
    data: dict = json.loads(request.body)
    uid = data.get('uid')
    aid = data.get('aid')
    user_activity.delete_relation(uid, aid)
    return JsonResponse({"msg": "活动已退出", "status": True})


@require_http_methods(["POST"])
def favor(request):
    """ 用户点赞活动 """
    data: dict = json.loads(request.body)
    method = data.get('method')
    user = User.objects.get(uid=data.get('uid'))
    activity = Activity.objects.get(aid=data.get('aid'))

    category = activity.category
    favor_rec = UserFavor.objects.filter(uid=user, category=category).first()
    participate_rec = UserInActivity.objects.get(uid=user, aid=activity)
    if method == "like":
        if participate_rec.like:
            return JsonResponse({"msg": "无法重复点赞", "status": False})
        else:
            participate_rec.like = True
            participate_rec.save()
        if favor_rec:
            favor_rec.cnt = favor_rec.cnt + 1
            favor_rec.save()
        else:
            new_rec = UserFavor(uid=user, category=category, cnt=1)
            new_rec.save()
        activity.favor = activity.favor + 1
        activity.save()
        return JsonResponse({"msg": "点赞成功", "status": True})
    elif method == "remove":
        if not participate_rec.like:
            return JsonResponse({"msg": "不存在点赞记录", "status": False})
        else:
            participate_rec.like = False
            participate_rec.save()
        if favor_rec:
            favor_rec.cnt = favor_rec.cnt - 1
            favor_rec.save() if favor_rec.cnt > 0 else favor_rec.delete()
            activity.favor = activity.favor - 1
            activity.save()
            return JsonResponse({"msg": "点赞已取消", "status": True})
        else:
            return JsonResponse({"msg": "不存在点赞记录", "status": False})
    else:
        return JsonResponse({"msg": "method参数有误", "status": False})


@require_http_methods(["GET"])
def recommend(request):
    uid = request.GET.get('uid')
    print(uid)
    lst = rcd.get_recommend_activity(uid)
    return JsonResponse({"msg": "推荐活动获取成功", "status": True, "list": lst})
