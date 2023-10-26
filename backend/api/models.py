from django.db import models


class User(models.Model):
    USER_GENDER = {
        (0, '女'),
        (1, '男'),
    }
    uid = models.IntegerField(primary_key=True)
    account = models.CharField(max_length=32, unique=True)
    pwd = models.CharField(max_length=32)
    user_name = models.CharField(max_length=10)
    user_age = models.IntegerField()
    user_gender = models.SmallIntegerField(choices=USER_GENDER)
    phone_number = models.BigIntegerField(unique=True)
    email = models.EmailField(max_length=32, unique=True)
    personal_signature = models.CharField(max_length=128, null=True, blank=True)
