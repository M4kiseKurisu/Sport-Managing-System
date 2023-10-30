from django.db import models
import django.utils.timezone as timezone


# ----------------------------  实体表  -------------------------------- #
class User(models.Model):
    """ 用户实体表 """
    USER_GENDER = {
        (0, '女'),
        (1, '男'),
    }
    uid = models.IntegerField(primary_key=True)
    account = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    user_name = models.CharField(max_length=10)
    user_age = models.IntegerField()
    user_gender = models.SmallIntegerField(choices=USER_GENDER)
    phone_number = models.BigIntegerField(unique=True)
    email = models.EmailField(max_length=32, unique=True)
    user_signature = models.CharField(max_length=128, null=True, blank=True)


class Group(models.Model):
    """ 团体实体表 """
    gid = models.IntegerField(primary_key=True)
    group_name = models.CharField(max_length=32, unique=True)
    group_desc = models.CharField(max_length=128)


# ----------------------------  联系表  -------------------------------- #
class UserInGroup(models.Model):
    """ 用户从属团体联系表 """
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    gid = models.ForeignKey(Group, on_delete=models.CASCADE)
    manager_flag = models.BooleanField()

    class Meta:
        unique_together = (("uid", "gid"),)


class UserApplyGroup(models.Model):
    """ 用户申请团体联系表 """
    STATUS = {
        (0, "申请中"),
        (1, "已接受"),
        (2, "已拒绝")
    }
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    gid = models.ForeignKey(Group, on_delete=models.CASCADE)
    content = models.CharField(max_length=128)
    apply_time = models.DateTimeField(default=timezone.now)
    status = models.CharField(choices=STATUS, max_length=8)

    class Meta:
        unique_together = (("uid", "gid", "apply_time"),)
