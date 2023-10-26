from django.urls import path
from api.views import user
urlpatterns = [
    path('login/', user.login),
]