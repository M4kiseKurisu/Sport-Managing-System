from django.urls import path

from api.views.entity import equipment
from api.views.entity import user
from api.views.entity import field
from api.views.entity import group

urlpatterns = [
    # user
    path('user/login', user.login),
    path('user/register', user.register),
    path('user/information', user.information),
    path('user/modify/text', user.modify_text),
    path('user/modify/pic', user.modify_pic),
    path('user/group', user.group_list),

    # group
    path('group/view', group.view),
    path('group/create', group.create),
    path('group/join', group.join),
    path('group/apply', group.apply),
    path('group/exit', group.exit_out),
    path('group/members/list', group.members_list),
    path('group/members/remove', group.members_remove),
    path('group/members/authority', group.members_authority),

    # field
    path('field/add', field.add),
    path('field/view', field.view),

    # equipment
    path('equipment/add', equipment.add),
    path('equipment/view', equipment.view),
    path('equipment/borrow', equipment.borrow),
    path('equipment/record', equipment.record),
    path('equipment/return', equipment.give_back),

    # friend
    path('user/find', user.find),
    path('friend/add', user.friend_add),
    path('friend/apply', user.friend_apply),
    path('friend/list', user.friend_list),
    path('friend/delete', user.friend_delete),
]
