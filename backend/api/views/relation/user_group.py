"""
用户和团体联系
"""
from django.db.models import Q

from api.models import UserInGroup
from api.models import UserApplyGroup
from api.models import User
from api.models import Group


def search_relation(uid, gid):
    """ 查询用户团体联系 """
    user = User.objects.filter(uid=uid).first()
    group = Group.objects.filter(gid=gid).first()
    if user and not group:
        return UserInGroup.objects.filter(uid=user)
    elif group and not user:
        return UserInGroup.objects.filter(gid=group)
    elif user and group:
        return UserInGroup.objects.filter(uid=user, gid=group)
    else:
        return None


def add_relation(uid, gid, teammate_type):
    """ 增加用户团体联系 """
    user = User.objects.filter(uid=uid).first()
    group = Group.objects.filter(gid=gid).first()
    if UserInGroup.objects.filter(uid=user, gid=group).first():
        return False
    else:
        new_relation = UserInGroup(uid=user, gid=group, type=teammate_type)
        new_relation.save()
        group.capacity += 1
        group.save()
        return True


def delete_relation(uid, gid):
    """ 删除用户团体联系 """
    user = User.objects.get(uid=uid)
    group = Group.objects.get(gid=gid)
    relation = UserInGroup.objects.filter(uid=user, gid=group).first()
    if relation:
        if relation.type == 0:
            group.delete()
        else:
            relation.delete()
            group.capacity -= 1
            group.save()


def modify_relation(uid, gid, member_type):
    user = User.objects.get(uid=uid)
    group = Group.objects.get(gid=gid)
    relation = UserInGroup.objects.get(uid=user, gid=group)
    relation.type = member_type
    relation.save()


def add_apply(uid, gid, content):
    """ 增加用户申请团体信息 """
    user = User.objects.get(uid=uid)
    group = Group.objects.get(gid=gid)

    if group.maximum == group.capacity:
        return "团体人数已达上限", False
    if UserApplyGroup.objects.filter(uid=user, gid=group, status=0).first():
        return "已有申请正在审核中，请耐心等待", False
    else:
        apply = UserApplyGroup(uid=user, gid=group, content=content, status=0)
        apply.save()
        return "申请信息已发送", True


def search_accept_apply(uid):
    """ 查找收到的团体申请信息 """
    lst = []
    user = User.objects.get(uid=uid)

    groups = list(map(lambda param: param.gid, UserInGroup.objects.filter(Q(uid=user) & (Q(type=0) | Q(type=1)))))
    for group in groups:
        applies = UserApplyGroup.objects.filter(gid=group).order_by('-apply_time')
        lst += list(applies)

    return lst


def search_send_apply(uid):
    """ 查找发送的团体申请信息 """
    user = User.objects.get(uid=uid)
    applies = UserApplyGroup.objects.filter(uid=user).order_by('-apply_time')
    print(applies)
    lst = list(applies)
    return lst


def handle_apply(uid, gid, res):
    """ 管理员处理团体申请请求 """
    group = Group.objects.get(gid=gid)
    applicant = User.objects.get(uid=uid)
    apply = UserApplyGroup.objects.get(uid=applicant, gid=group, status=0)
    if res:
        if group.capacity == group.maximum:
            return False
        apply.status = 1
        group.capacity += 1
        group.save()
        rec = UserInGroup(uid=applicant, gid=group, type=2)
        rec.save()
    else:
        apply.status = 2
    apply.save()
    return True
