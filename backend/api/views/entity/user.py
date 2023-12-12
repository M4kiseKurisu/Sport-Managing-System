"""
用户实体
"""
import json
import random

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.db.models import Q
from django.utils import timezone
from datetime import timedelta

from api.models import User
from api.models import ActivityUseField
from api.models import UserInActivity
from api.views.relation import user_group, friend


def genid():
    new_id = random.randint(0, 99999999)
    while User.objects.filter(uid=new_id):
        new_id = random.randint(0, 99999999)
    return new_id


@require_http_methods(["GET"])
def login(request):
    """ 用户登录验证 """
    account = request.GET.get('account')
    password = request.GET.get('password')
    user = User.objects.filter(account=account, password=password).first()
    if user:
        return JsonResponse({"msg": '登录成功', "status": True, "uid": user.uid, "user_name": user.user_name,
                             "picture": user.picture.url if user.picture else None})
    else:
        return JsonResponse({"msg": '登录失败', "status": False, "uid": None, "user_name": None})


@require_http_methods(["POST"])
def register(request):
    """ 用户注册 """
    data: dict = json.loads(request.body)
    account = data.get('account')
    phone_number = data.get("phone_number")
    email = data.get("email")
    if User.objects.filter(account=account).first():
        return JsonResponse({"msg": "账号已被注册", "status": False, "uid": "", "user_name": ""})
    elif User.objects.filter(Q(phone_number=phone_number) | Q(email=email)).first():
        return JsonResponse({"msg": "电话或邮箱已被注册", "status": False, "uid": "", "user_name": ""})
    else:
        uid = genid()
        password = data.get('password')
        user_name = data.get('user_name')
        user_age = data.get("user_age")
        user_gender = data.get("user_gender")
        user_signature = ""
        new_user = User(uid=uid, account=account, password=password, user_name=user_name,
                        user_age=user_age, user_gender=user_gender, phone_number=phone_number,
                        email=email, user_signature=user_signature)
        new_user.save()
        return JsonResponse({"msg": "注册成功", "status": True, "uid": uid, "user_name": user_name})


@require_http_methods(["GET"])
def information(request):
    """ 查看用户基本信息 """
    uid = request.GET.get('uid')
    user = User.objects.get(uid=uid)

    # 用户参加的活动：
    activities = UserInActivity.objects.filter(uid=uid)
    # 用户参加的团体
    groups = user_group.search_relation(uid, None)
    # 用户的好友
    f = friend.search_relation(uid)

    info = {"uid": uid, "name": user.user_name, "age": user.user_age,
            "gender": user.get_user_gender_display(), "phone": user.phone_number, "email": user.email,
            "signature": user.user_signature, "picture": user.picture.url if user.picture else None,
            "activity": len(activities), "friend": len(f), "group": len(groups)}
    print(info)
    return JsonResponse({"msg": '个人基本信息获取成功', "status": True, "info": info})


@require_http_methods(["POST"])
def modify_text(request):
    """ 修改个人信息 """
    req: dict = json.loads(request.body)
    print(req)
    user = User.objects.get(uid=req.get('uid'))
    # 数据库约束检查
    phone_number = req.get('data').get('phone_number')
    email = req.get('data').get('email')
    if phone_number and phone_number != user.phone_number:
        if User.objects.filter(phone_number=phone_number).first():
            return JsonResponse({"msg": "电话号码已存在", "status": False})
    if email and email != user.email:
        if User.objects.filter(email=email).first():
            return JsonResponse({"msg": "邮箱已存在", "status": False})

    for (key, value) in req.get('data').items():
        print(key, value)
        setattr(user, key, value)
    user.save()
    return JsonResponse({"msg": "个人信息修改成功", "status": True})


@require_http_methods(["POST"])
def modify_pic(request):
    """ 修改个人头像 """
    print(request.POST)
    user = User.objects.get(uid=request.POST.get('uid'))
    user.picture = request.FILES['picture']
    user.save()
    return JsonResponse({"msg": "头像已更新", "status": True})


@require_http_methods(["GET"])
def group_list(request):
    """ 查看用户所属团体 """
    uid = request.GET.get('uid')
    lst = list(map(lambda param: {'gid': param.gid.gid, 'group_name': param.gid.group_name,
                                  'group_desc': param.gid.group_desc, 'tag': param.gid.tag,
                                  'capacity': param.gid.capacity, 'maximum': param.gid.maximum,
                                  'creator': param.gid.creator.user_name,
                                  'pic': param.gid.picture.url if param.gid.picture else None,
                                  "type": param.get_type_display()},
                   user_group.search_relation(uid, None)))
    print(lst)
    return JsonResponse({"msg": '团体信息请求成功', "status": True, "list": lst})


@require_http_methods(["GET"])
def find(request):
    """ 查询用户 """
    key = request.GET.get('keyword', '')
    if key == '':
        lst = []
    else:
        users = User.objects.filter(user_name__icontains=key)
        friends = friend.search_relation(request.GET.get('uid'))
        lst = list(map(lambda param: {'uid': param.uid, 'user_name': param.user_name,
                                      "pic": param.picture.url if param.picture else None,
                                      "signature": param.user_signature, "is_friend": param in friends},
                       users))
    print(lst)
    return JsonResponse({"msg": '用户信息搜索成功', "status": True, "list": lst})


@require_http_methods(["GET"])
def friend_list(request):
    """ 好友列表 """
    uid = request.GET.get('uid')
    keyword = request.GET.get('keyword', '')

    lst = []
    for param in friend.search_relation(uid):
        if keyword in param.user_name:
            lst.append({'uid': param.uid, 'user_name': param.user_name,
                        "pic": param.picture.url if param.picture else None,
                        "signature": param.user_signature})
    print(lst)
    return JsonResponse({"msg": '好友列表请求成功', "status": True, "list": lst})


@require_http_methods(["POST"])
def friend_add(request):
    """ 申请添加好友 """
    data: dict = json.loads(request.body)
    print(data)
    sender = data.get('sender')
    receiver = data.get('receiver')
    content = data.get('content')
    msg, status = friend.add_apply(sender, receiver, content)
    return JsonResponse({"msg": msg, "status": status})


@require_http_methods(["POST", "GET"])
def friend_apply(request):
    if request.method == 'GET':
        """ 查看好友申请 """
        uid = request.GET.get('uid')
        method = request.GET.get('method')

        if method == "accept":
            applies = friend.search_accept_apply(uid)
            lst = list(map(lambda param: {"uid": param.sender.uid, "user_name": param.sender.user_name,
                                          "content": param.content, "status": param.get_status_display(),
                                          "time": param.apply_time.strftime("%Y-%m-%d %H:%M:%S")},
                           applies))
        elif method == "send":
            applies = friend.search_send_apply(uid)
            lst = list(map(lambda param: {"uid": param.receiver.uid, "user_name": param.receiver.user_name,
                                          "content": param.content, "status": param.get_status_display(),
                                          "time": param.apply_time.strftime("%Y-%m-%d %H:%M:%S")},
                           applies))
        else:
            return JsonResponse({"msg": "method参数错误", "status": False})

        return JsonResponse({"msg": "好友申请信息获取成功", "status": True, "list": lst})

    elif request.method == 'POST':
        """ 处理好友申请 """
        data: dict = json.loads(request.body)
        print(data)
        friend.handle_apply(data.get('sender'), data.get('receiver'), data.get('res'))
        return JsonResponse({"msg": "处理完成", "status": True})


@require_http_methods(["POST"])
def friend_delete(request):
    """ 用户删除好友 """
    data: dict = json.loads(request.body)
    print(data)
    uid = data.get('uid')
    fid = data.get('fid')
    friend.delete_relation(uid, fid)
    return JsonResponse({"msg": '好友删除完成', "status": True})


@require_http_methods(["GET"])
def activity_list(request):
    """ 查看用户参加的活动 """
    uid = request.GET.get('uid')
    user = User.objects.get(uid=uid)
    activities = set()
    liked_activities = set()
    for rec in UserInActivity.objects.filter(uid=user):
        if rec.like:
            liked_activities.add(rec.aid)
        activities.add(rec.aid)
    lst = list(map(lambda param: {"aid": param.aid.aid, "name": param.aid.name, "type": param.aid.get_type_display(),
                                  "private": param.aid.private, "category": param.aid.category,
                                  "capacity": param.aid.capacity, "maximum": param.aid.maximum,
                                  "picture": param.aid.picture.url if param.aid.picture else None,
                                  "start_time": param.start_time.strftime("%Y-%m-%d %H:%M:%S"),
                                  "end_time": param.end_time.strftime("%Y-%m-%d %H:%M:%S"),
                                  "favor": param.aid.favor, "is_favor": param.aid in liked_activities},
                   ActivityUseField.objects.filter(aid__in=activities).order_by('-start_time')))
    print(lst)
    return JsonResponse({"msg": '活动信息获取成功', "status": True, "list": lst})


@require_http_methods(["GET"])
def activity_statistic(request):
    """ 用户参加的活动数量统计 """
    uid = request.GET.get('uid')
    user = User.objects.get(uid=uid)
    records = UserInActivity.objects.filter(uid=user)
    statistic = dict()
    for record in records:
        category = record.aid.category
        statistic[category] = statistic.get(category, 0) + 1
    print(statistic)
    return JsonResponse({"msg": '活动统计信息获取成功', "status": True, "data": statistic})


@require_http_methods(["GET"])
def activity_arrangement(request):
    """ 用户未来七天活动安排 """
    uid = request.GET.get('uid')
    user = User.objects.get(uid=uid)

    # 获取当前日期范围
    now = timezone.now()
    start_of_today = now.replace(hour=0, minute=0, second=0, microsecond=0)
    end_of_7_days = start_of_today + timedelta(days=7)

    # 用户参加的活动
    activities = set()
    for rec in UserInActivity.objects.filter(uid=user):
        activities.add(rec.aid)

    records = ActivityUseField.objects.filter(
        aid__in=activities,
        start_time__gte=start_of_today,
        end_time__lt=end_of_7_days
    ).order_by('start_time')

    data = dict()
    for rec in records:
        data.setdefault(rec.start_time.strftime("%Y-%m-%d"), []).append(rec.aid.name)
    return JsonResponse({"msg": '活动安排获取成功', "status": True, "data": data})


@require_http_methods(["GET"])
def group_statistic(request):
    """ 用户参加的团体统计 """
    uid = request.GET.get('uid')
    records = user_group.search_relation(uid, None)
    statistic = dict()

    for record in records:
        tag = record.gid.tag
        statistic[tag] = statistic.get(tag, 0) + 1
    print(statistic)
    return JsonResponse({"msg": '团体统计信息获取成功', "status": True, "data": statistic})
