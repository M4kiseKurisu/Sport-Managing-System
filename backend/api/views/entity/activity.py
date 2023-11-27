"""
活动实体
"""
import json
import random

from django.http import JsonResponse
from django.db.models import Q
from django.views.decorators.http import require_http_methods

from api.models import Activity
from api.models import User
from api.views.relation import user_activity


def genid():
    new_id = random.randint(0, 99999999)
    while Activity.objects.filter(aid=new_id):
        new_id = random.randint(0, 99999999)
    return new_id


