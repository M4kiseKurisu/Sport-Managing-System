from django.http import JsonResponse
from api.models import User


def login(request):
    account = request.GET.get('account')
    pwd = request.GET.get('pwd')
    user = User.objects.filter(account=account, pwd=pwd).first()
    if user:
        return JsonResponse({"res": True, "msg": '登录成功', "id": user.uid, "user_name": user.user_name})
    else:
        return JsonResponse({"res": False, "msg": '登录失败', "id": '000000', "user_name": None})
