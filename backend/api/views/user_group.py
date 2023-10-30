"""
管理用户和团体联系
"""
from api.models import UserInGroup
from api.models import UserApplyGroup
from api.models import User
from api.models import Group


def add_relation(uid, gid, is_manager):
    """ 增加用户团体联系 """
    u = User.objects.filter(uid=uid).first()
    g = Group.objects.filter(gid=gid).first()
    if UserInGroup.objects.filter(uid=u, gid=g).first():
        return False
    else:
        new_relation = UserInGroup(uid=u, gid=g, manager_flag=is_manager)
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
    u = User.objects.filter(uid=uid).first()
    g = Group.objects.filter(gid=gid).first()
    print(UserApplyGroup.objects.filter(uid=u, gid=g, status=0).first())
    if UserApplyGroup.objects.filter(uid=u, gid=g, status=0).first():
        return False
    else:
        apply = UserApplyGroup(uid=u, gid=g, content=content, status=0)
        print(apply)
        apply.save()
        return True


def search_apply(uid, is_manager):
    """ 查找团体申请信息 """
    lst = []
    u = User.objects.get(uid=uid)
    if is_manager:
        gids = UserInGroup.objects.filter(uid=u, manager_flag=True).values('gid')
        print(gids)
        for gid in gids:
            lst.extend(list(UserApplyGroup.objects.values('uid', 'gid', 'content')
                            .filter(gid=gid, status=0)))
    else:
        lst.extend(UserApplyGroup.objects.filter(uid=u, status=0))
    return lst
