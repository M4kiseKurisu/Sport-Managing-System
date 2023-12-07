from django.urls import path

from api.views.entity import equipment
from api.views.entity import user
from api.views.entity import field
from api.views.entity import group
from api.views.entity import notice
from api.views.entity import activity
from api.views.entity import stream

urlpatterns = [
    # user
    path('user/login', user.login),
    path('user/register', user.register),
    path('user/information', user.information),
    path('user/modify/text', user.modify_text),
    path('user/modify/pic', user.modify_pic),
    path('user/group', user.group_list),
    path('user/activity/statistic', user.activity_statistic),
    path('user/activity/view', user.activity_list),

    # group
    path('group/view', group.view),
    path('group/create', group.create),
    path('group/join', group.join),
    path('group/apply', group.apply),
    path('group/exit', group.exit_out),
    path('group/members/list', group.members_list),
    path('group/members/remove', group.members_remove),
    path('group/members/authority', group.members_authority),
    path('group/activity/statistic', group.activity_statistic),
    path('group/activity/view', group.activity_list),

    # field
    path('field/add', field.add),
    path('field/view', field.view),
    path('field/usage', field.usage),

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

    # activity
    path('activity/create', activity.create),
    path('activity/detail', activity.detail),
    path('activity/view/active', activity.active),
    path('activity/view/inactive', activity.inactive),
    path('activity/join', activity.join),
    path('activity/exit', activity.exit_out),
    path('activity/favor', activity.favor),
    path('activity/recommend', activity.recommend),

    # notice
    path('notice/list', notice.notice_list),
    path('notice/confirm', notice.notice_confirm),

    # stream
    path('stream/publish', stream.publish),
    path('stream/delete', stream.remove),
    path('stream/favor', stream.favor),
    path('stream/view', stream.view),

]
