"""
动态实体
"""
import json
import random

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.db.models import Q
from django.utils.dateparse import parse_date

from api.models import User
from api.models import Stream
from api.models import Activity
from api.models import UserFavorStream
from api.views.relation import friend


def genid():
    new_id = random.randint(0, 99999999)
    while Stream.objects.filter(sid=new_id):
        new_id = random.randint(0, 99999999)
    return new_id


@require_http_methods(["POST"])
def publish(request):
    """ 用户发布动态 """
    data = request.POST
    print(data)
    user = User.objects.get(uid=data.get('uid'))
    activity = Activity.objects.get(aid=data.get('aid'))
    if request.FILES.get('picture'):
        new_stream = Stream(sid=genid(), text=data.get('text'), picture=request.FILES['picture'],
                            favor=0, private=data.get('private'), user=user, activity=activity)
        new_stream.save()
    else:
        new_stream = Stream(sid=genid(), text=data.get('text'), favor=0, private=data.get('private'),
                            user=user, activity=activity)
        new_stream.save()
    return JsonResponse({"msg": "动态发布成功", "status": True})


@require_http_methods(["POST"])
def remove(request):
    """ 用户删除动态 """
    data: dict = json.loads(request.body)
    stream = Stream.objects.filter(sid=data.get('sid'))
    stream.delete()
    return JsonResponse({"msg": "动态删除成功", "status": True})


@require_http_methods(["POST"])
def favor(request):
    """ 点赞或取消 """
    data: dict = json.loads(request.body)
    user = User.objects.get(uid=data.get('uid'))
    stream = Stream.objects.get(sid=data.get('sid'))
    rec = UserFavorStream.objects.filter(uid=user, sid=stream).first()
    if rec:
        stream.favor -= 1
        rec.delete()
    else:
        stream.favor += 1
        rec = UserFavorStream(uid=user, sid=stream)
        rec.save()
    stream.save()
    return JsonResponse({"msg": "操作成功", "status": True})


@require_http_methods(["GET"])
def view(request):
    """ 查看动态列表 """
    user = User.objects.get(uid=request.GET.get('uid'))
    time = request.GET.get('time', '')
    query = Q()
    if time:
        query &= Q(time__date=parse_date(time))
    # 好友
    friends = friend.search_relation(request.GET.get('uid'))
    # 可见的动态
    streams = set()
    for rec in Stream.objects.filter(query).order_by('-time'):
        if rec.user == user:
            streams.add(rec)
        elif rec.private == 1 and rec.user in friends:
            streams.add(rec)
        elif rec.private == 2:
            streams.add(rec)
    # 点赞的动态
    like_stream_user = dict()
    liked_stream = set()
    for rec in UserFavorStream.objects.all():
        if rec.sid in streams:
            like_stream_user.setdefault(str(rec.sid.sid), []).append(
                {"uid": rec.uid.uid, "user_name": rec.uid.user_name})
            if rec.uid == user:
                liked_stream.add(rec.sid)

    lst = list(map(lambda param: {"owner": {"check": param.user == user, "name": param.user.user_name,
                                            "picture": param.picture.url if param.picture else None},
                                  "sid": param.sid, "time": param.time.strftime("%Y-%m-%d %H:%M:%S"),
                                  "text": param.text, "picture": param.picture.url if param.picture else None,
                                  "favor": param.favor, "is_favor": param in liked_stream,
                                  "liker": like_stream_user.get(str(param.sid), []),
                                  "private": param.get_private_display(),
                                  "aid": param.activity.aid, "activity_name": param.activity.name},
                   streams))
    return JsonResponse({"msg": "动态列表获取成功", "status": True, "list": lst})
