from django.db import models


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


class Field(models.Model):
    """ 运动场地实体表 """
    fid = models.IntegerField(primary_key=True)
    location = models.CharField(max_length=32, unique=True)
    category = models.CharField(max_length=16)
    limit = models.BooleanField()
    open_time = models.TimeField()
    close_time = models.TimeField()


class Activity(models.Model):
    """ 活动项目实体表 """
    aid = models.IntegerField(primary_key=True)
    activity_name = models.CharField(max_length=32)
    activity_desc = models.CharField(max_length=128)


class Equipment(models.Model):
    """ 器材实体表 """
    eid = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=32, unique=True)
    amount = models.IntegerField(default=0)


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
        (2, "已拒绝"),
    }
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    gid = models.ForeignKey(Group, on_delete=models.CASCADE)
    content = models.CharField(max_length=128)
    apply_time = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(choices=STATUS)

    class Meta:
        unique_together = (("uid", "gid", "apply_time"),)


class ActivityUseField(models.Model):
    """ 活动使用场地联系表"""
    aid = models.ForeignKey(Activity, on_delete=models.CASCADE)
    fid = models.ForeignKey(Field, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = (("aid",), ("fid", "start_time"), ("fid", "end_time"),)


class UserInActivity(models.Model):
    """ 用户参加项目联系表 """
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    aid = models.ForeignKey(Activity, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("uid", "aid"),)


class UserCreateActivity(models.Model):
    """ 用户发起活动联系表 """
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    aid = models.ForeignKey(Activity, on_delete=models.CASCADE)
    private = models.BooleanField()

    class Meta:
        unique_together = (("aid",),)


class GroupCreateActivity(models.Model):
    """ 团体发起活动联系表 """
    gid = models.ForeignKey(Group, on_delete=models.CASCADE)
    aid = models.ForeignKey(Activity, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("aid",),)


class UserEquipment(models.Model):
    """ 用户借用器材联系表 """
    eid = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    lend_time = models.DateTimeField()
    lend_amount = models.IntegerField()
    is_return = models.BooleanField(default=False)

    class Meta:
        unique_together = (("eid", "uid", "lend_time"),)


class GroupEquipment(models.Model):
    """ 团体借用器材联系表 """
    eid = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    gid = models.ForeignKey(Group, on_delete=models.CASCADE)
    lend_time = models.DateTimeField()
    lend_amount = models.IntegerField()
    is_return = models.BooleanField()

    class Meta:
        unique_together = (("eid", "gid", "lend_time"),)
