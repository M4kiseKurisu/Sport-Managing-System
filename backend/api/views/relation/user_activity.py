"""
用户和活动联系
"""
from django.db.models import Q

from api.models import User
from api.models import Activity
from api.models import UserInActivity

def search_relation(uid):
    """ 查询用户活动联系 """
    user = User.objects.filter(uid=uid).first()
    if user:
        return UserInActivity.objects.filter(uid=user)
    else:
        return None