"""
管理用户和团体联系
"""
from django.db.models import Q

from api.models import UserInGroup
from api.models import UserApplyGroup
from api.models import User
from api.models import Group


def search_relation(uid):
    """ 查询用户团体联系 """
    user = User.objects.filter(uid=uid).first()
    if user:
        return UserInGroup.objects.filter(uid=user)
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
        return True


def delete_relation(uid, gid):
    """ 删除用户团体联系 """
    if UserInGroup.objects.filter(uid=uid, gid=gid).first():
        return True
    else:
        return False


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


def search_apply(uid, is_manager):
    """ 查找团体申请信息 """
    lst = []
    user = User.objects.get(uid=uid)

    if is_manager:
        groups = list(map(lambda param: param.gid, UserInGroup.objects.filter(Q(uid=user) & (Q(type=0) | Q(type=1)))))
        for group in groups:
            applies = UserApplyGroup.objects.filter(gid=group, status=0).order_by('-apply_time')
            for apply in applies:
                temp = {"uid": apply.uid.uid, "user_name": apply.uid.user_name, "content": apply.content,
                        "gid": group.gid, "group_name": group.group_name,
                        "time": apply.apply_time.strftime("%Y-%m-%d %H:%M:%S")}
                lst.append(temp)
    else:
        applies = UserApplyGroup.objects.filter(uid=user).order_by('-apply_time')
        print(applies)
        for apply in applies:
            temp = {"gid": apply.gid.gid, "group_name": apply.gid.group_name,
                    "time": apply.apply_time.strftime("%Y-%m-%d %H:%M:%S"),
                    "status": apply.get_status_display()}
            lst.append(temp)

    return lst


def handle_apply(mid, uid, gid, res):
    """ 管理员处理团体申请请求 """
    manager = User.objects.get(uid=mid)
    group = Group.objects.get(gid=gid)
    if not UserInGroup.objects.get(uid=manager, gid=group, manager_flag=True):
        return False
    else:
        applicant = User.objects.get(uid=uid)
        apply = UserApplyGroup.objects.get(uid=applicant, gid=group)
        if res:
            apply.status = 1
            rec = UserInGroup(uid=applicant, gid=group, manager_flag=False)
            rec.save()
        else:
            apply.status = 2
        apply.save()
        return True
