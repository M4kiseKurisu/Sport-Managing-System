"""
管理用户实体
"""
import json
import random
from django.http import JsonResponse
from django.db.models import Q

from api.models import User


def genid():
    new_id = random.randint(0, 99999999)
    while User.objects.filter(uid=new_id):
        new_id = random.randint(0, 99999999)
    return new_id


def login(request):
    if request.method == 'GET':
        account = request.GET.get('account')
        password = request.GET.get('password')
        user = User.objects.filter(account=account, password=password).first()
        if user:
            return JsonResponse({"msg": '登录成功', "res": True, "uid": user.uid, "user_name": user.user_name})
        else:
            return JsonResponse({"msg": '登录失败', "res": False, "uid": None, "user_name": None})
    else:
        return JsonResponse({"msg": "请求方式有误"})


def register(request):
    if request.method == 'POST':
        data: dict = json.loads(request.body)
        account = data.get('account')
        phone_number = data.get("phone_number")
        email = data.get("email")
        if User.objects.filter(account=account).first():
            return JsonResponse({"msg": "账号已被注册", "uid": "", "user_name": ""})
        elif User.objects.filter(Q(phone_number=phone_number) | Q(email=email)).first():
            return JsonResponse({"msg": "电话或邮箱已被注册", "uid": "", "user_name": ""})
        else:
            uid = genid()
            password = data.get('password')
            user_name = data.get('user_name')
            user_age = data.get("user_age")
            user_gender = data.get("user_gender")
            user_signature = data.get("user_signature")
            new_user = User(uid=uid, account=account, password=password, user_name=user_name,
                            user_age=user_age, user_gender=user_gender, phone_number=phone_number,
                            email=email, user_signature=user_signature)
            new_user.save()
            return JsonResponse({"msg": "注册成功", "uid": uid, "user_name": user_name})
    else:
        return JsonResponse({"msg": "请求方式有误"})
