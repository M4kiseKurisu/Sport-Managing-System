"""
用户实体
"""
import json
import random
from django.http import JsonResponse
from django.db.models import Q

from api.models import User

from api.views import user_group
from api.views import user_activity
from api.views import friends


def genid():
    new_id = random.randint(0, 99999999)
    while User.objects.filter(uid=new_id):
        new_id = random.randint(0, 99999999)
    return new_id


def login(request):
    """ 用户登录验证 """
    if request.method == 'GET':
        account = request.GET.get('account')
        password = request.GET.get('password')
        user = User.objects.filter(account=account, password=password).first()
        if user:
            return JsonResponse({"msg": '登录成功', "status": True, "uid": user.uid, "user_name": user.user_name,
                                 "picture": user.picture.url})
        else:
            return JsonResponse({"msg": '登录失败', "status": False, "uid": None, "user_name": None})
    else:
        return JsonResponse({"msg": "请求方式有误", "status": False})


def register(request):
    """ 用户注册 """
    if request.method == 'POST':
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
    else:
        return JsonResponse({"msg": "请求方式有误", "status": False})


def information(request):
    """ 查看用户基本信息 """
    if request.method == 'GET':
        uid = request.GET.get('uid')
        user = User.objects.get(uid=uid)

        # 用户参加的活动：
        activities = user_activity.search_relation(uid)
        # 用户参加的团体
        groups = user_group.search_relation(uid)
        # 用户的好友
        f = friends.search_relation(uid)

        info = {"uid": uid, "name": user.user_name, "age": user.user_age,
                "gender": user.get_user_gender_display(), "phone": user.phone_number, "email": user.email,
                "signature": user.user_signature, "picture": user.picture.url if user.picture else None,
                "activity": len(activities), "friend": len(f), "group": len(groups)}
        print(info)
        return JsonResponse({"msg": '个人基本信息获取成功', "status": True, "info": info})

    else:
        return JsonResponse({"msg": "请求方式有误", "status": False})


def modify_text(request):
    """ 修改个人信息 """
    if request.method == 'POST':
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
    else:
        return JsonResponse({"msg": "请求方式有误", "status": False})


def modify_pic(request):
    """ 修改个人头像 """
    print(request.POST)
    user = User.objects.get(uid=request.POST.get('uid'))
    user.picture = request.FILES['picture']
    user.save()
    return JsonResponse({"msg": "头像已更新", "status": True})


def group_view(request):
    """ 查看用户所属团体 """
    if request.method == 'GET':
        uid = request.GET.get('uid')
        lst = list(map(lambda param: {'gid': param.gid.gid, 'group_name': param.gid.group_name,
                                      "pic": param.gid.picture.url if param.gid.picture else None,
                                      "type": param.get_type_display()},
                       user_group.search_relation(uid)))
        print(lst)
        return JsonResponse({"msg": '团体信息请求成功', "status": True, "list": lst})
    else:
        return JsonResponse({"msg": "请求方式有误", "status": False})
