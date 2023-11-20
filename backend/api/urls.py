from django.urls import path

from api.views import user
from api.views import group
from api.views import field
from api.views import equipment

urlpatterns = [
    # user
    path('user/login', user.login),
    path('user/register', user.register),
    path('user/group', user.group_view),

    # group
    path('group/view', group.view),
    path('group/create', group.create),
    path('group/join', group.join),
    path('group/apply', group.apply),

    # field
    path('field/add', field.add),
    path('field/view', field.view),

    # equipment
    path('equipment/add', equipment.add),
    path('equipment/view', equipment.view),
    path('equipment/borrow', equipment.borrow),
    path('equipment/record', equipment.record),
    path('equipment/return', equipment.give_back)
]
