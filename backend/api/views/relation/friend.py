"""
好友联系
"""

from django.db.models import Q

from api.models import User
from api.models import Friend
from api.models import FriendApply


def search_relation(uid):
    """ 查询用户的好友 """
    lst = []
    user = User.objects.filter(uid=uid).first()
    if user:
        lst += list(map(lambda param: param.uid2, Friend.objects.filter(uid1=user)))
        lst += list(map(lambda param: param.uid1, Friend.objects.filter(uid2=user)))
        return lst
    else:
        return None


def delete_relation(uid1, uid2):
    """ 删除好友联系 """
    user1 = User.objects.get(uid=uid1)
    user2 = User.objects.get(uid=uid2)
    Friend.objects.filter(
        Q(uid1=user1, uid2=user2) |
        Q(uid1=user2, uid2=user1)
    ).delete()


def add_apply(sid, rid, content):
    """ 添加好友申请信息 """
    sender = User.objects.get(uid=sid)
    receiver = User.objects.get(uid=rid)

    if FriendApply.objects.filter(sender=sender, receiver=receiver, status=0).first():
        return "已有申请正在审核中，请耐心等待", False
    else:
        apply = FriendApply(sender=sender, receiver=receiver, content=content, status=0)
        apply.save()
        return "申请信息已发送", True


def search_accept_apply(uid):
    """ 查看收到的好友申请 """
    user = User.objects.get(uid=uid)
    lst = list(FriendApply.objects.filter(receiver=user).order_by('-apply_time'))
    return lst


def search_send_apply(uid):
    """ 查看发送的好友申请 """
    user = User.objects.get(uid=uid)
    lst = list(FriendApply.objects.filter(sender=user).order_by('-apply_time'))
    return lst


def handle_apply(sid, rid, res):
    """ 用户处理好友申请 """
    sender = User.objects.get(uid=sid)
    receiver = User.objects.get(uid=rid)
    apply = FriendApply.objects.get(sender=sender, receiver=receiver, status=0)
    if res:
        apply.status = 1
        friendship = Friend(uid1=receiver, uid2=sender)
        friendship.save()
    else:
        apply.status = 2
    apply.save()
