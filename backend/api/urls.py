from django.urls import path

from api.views import user
from api.views import group
from api.views import field

urlpatterns = [
    path('user/login', user.login),
    path('user/register', user.register),

    path('group/create', group.create),
    path('group/join', group.join),
    path('group/apply', group.apply),

    path('field/add', field.add),
    path('field/search', field.search)
]
