from django.db import models

from api.system.storage import ImageStorage


# ----------------------------  实体表  -------------------------------- #
class User(models.Model):
    """ 用户实体表 """
    USER_GENDER = (
        (0, '女'),
        (1, '男'),
    )
    uid = models.IntegerField(primary_key=True)
    account = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    user_name = models.CharField(max_length=10)
    user_age = models.IntegerField()
    user_gender = models.SmallIntegerField(choices=USER_GENDER)
    phone_number = models.BigIntegerField(unique=True)
    email = models.EmailField(max_length=32, unique=True)
    user_signature = models.CharField(max_length=128, default="", blank=True)
    picture = models.ImageField(upload_to='images/user/', storage=ImageStorage(), null=True)


class Group(models.Model):
    """ 团体实体表 """
    gid = models.IntegerField(primary_key=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=32, unique=True)
    group_desc = models.CharField(max_length=128)
    tag = models.CharField(max_length=32)
    maximum = models.IntegerField()
    capacity = models.IntegerField()
    picture = models.ImageField(upload_to='images/group/', storage=ImageStorage(), null=True)


class Field(models.Model):
    """ 运动场地实体表 """
    fid = models.IntegerField(primary_key=True)
    location = models.CharField(max_length=32, unique=True)
    category = models.CharField(max_length=16, db_index=True)
    limit = models.BooleanField()
    open_time = models.TimeField()
    close_time = models.TimeField()


class Activity(models.Model):
    """ 活动项目实体表 """
    TYPE = (
        (0, "个人"),
        (1, "团体"),
    )
    aid = models.IntegerField(primary_key=True)
    type = models.SmallIntegerField(choices=TYPE, db_index=True)
    name = models.CharField(max_length=32, db_index=True)
    desc = models.CharField(max_length=128)
    category = models.CharField(max_length=32, db_index=True)
    tags = models.CharField(max_length=128)
    maximum = models.IntegerField()
    capacity = models.IntegerField()
    favor = models.IntegerField()
    picture = models.ImageField(upload_to='images/activity/', storage=ImageStorage(), null=True)
    private = models.BooleanField()


class Equipment(models.Model):
    """ 器材实体表 """
    eid = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=32, unique=True)
    amount = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='images/equipment/', storage=ImageStorage(), null=True)


class Stream(models.Model):
    """ 动态表 """
    PRIVACY = (
        (0, "仅自己可见"),
        (1, "好友可见"),
        (2, "所有人可见"),
    )
    sid = models.IntegerField(primary_key=True)
    time = models.DateTimeField(auto_now_add=True, db_index=True)
    text = models.CharField(max_length=512)
    picture = models.ImageField(upload_to='images/stream/', storage=ImageStorage(), null=True)
    favor = models.IntegerField(default=0)
    private = models.SmallIntegerField(choices=PRIVACY)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)


class Notice(models.Model):
    """ 系统通知表 """
    nid = models.IntegerField(primary_key=True)
    time = models.DateTimeField(auto_now_add=True, db_index=True)
    text = models.CharField(max_length=128)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)


# ----------------------------  联系表  -------------------------------- #
class UserInGroup(models.Model):
    """ 用户从属团体联系表 """
    TYPE = (
        (0, "创建人"),
        (1, "管理员"),
        (2, "成员"),
    )
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    gid = models.ForeignKey(Group, on_delete=models.CASCADE, db_index=True)
    type = models.SmallIntegerField(choices=TYPE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['uid', 'gid'], name='unique_user_in_group'),
        ]


class UserApplyGroup(models.Model):
    """ 用户申请团体联系表 """
    STATUS = (
        (0, "申请中"),
        (1, "已接受"),
        (2, "已拒绝"),
    )
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    gid = models.ForeignKey(Group, on_delete=models.CASCADE, db_index=True)
    content = models.CharField(max_length=128)
    apply_time = models.DateTimeField(auto_now_add=True, db_index=True)
    status = models.SmallIntegerField(choices=STATUS)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['uid', 'gid', 'apply_time'], name='unique_user_apply_group'),
        ]


class ActivityUseField(models.Model):
    """ 活动使用场地联系表"""
    aid = models.ForeignKey(Activity, on_delete=models.CASCADE)
    fid = models.ForeignKey(Field, on_delete=models.CASCADE)
    start_time = models.DateTimeField(db_index=True)
    end_time = models.DateTimeField(db_index=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['aid'], name='unique_activity_user_field1'),
            models.UniqueConstraint(fields=['fid', 'start_time'], name='unique_activity_user_field2'),
            models.UniqueConstraint(fields=['fid', 'end_time'], name='unique_activity_user_field3')
        ]


class UserInActivity(models.Model):
    """ 用户参加项目联系表 """
    uid = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    aid = models.ForeignKey(Activity, on_delete=models.CASCADE, db_index=True)
    like = models.BooleanField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['uid', 'aid'], name='unique_user_in_activity')
        ]


class UserCreateActivity(models.Model):
    """ 用户发起活动联系表 """
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    aid = models.ForeignKey(Activity, on_delete=models.CASCADE, db_index=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['aid'], name='unique_user_create_activity')
        ]


class GroupCreateActivity(models.Model):
    """ 团体发起活动联系表 """
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    gid = models.ForeignKey(Group, on_delete=models.CASCADE)
    aid = models.ForeignKey(Activity, on_delete=models.CASCADE, db_index=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['aid'], name='unique_group_create_activity')
        ]


class UserEquipment(models.Model):
    """ 用户借用器材联系表 """
    RETURN_STATUS = (
        (0, "未归还"),
        (2, "已归还"),
    )
    eid = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    uid = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    lend_amount = models.IntegerField()
    is_return = models.SmallIntegerField(choices=RETURN_STATUS, default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['eid', 'uid', 'start_time', 'end_time'], name='unique_user_equipment')
        ]


class GroupEquipment(models.Model):
    """ 团体借用器材联系表 """
    RETURN_STATUS = (
        (0, "未归还"),
        (2, "已归还"),
    )
    eid = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    gid = models.ForeignKey(Group, on_delete=models.CASCADE, db_index=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    lend_amount = models.IntegerField()
    is_return = models.SmallIntegerField(choices=RETURN_STATUS, default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['eid', 'gid', 'start_time', 'end_time'], name='unique_group_equipment')
        ]


class Friend(models.Model):
    """ 好友联系表 """
    uid1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends1')
    uid2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends2')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['uid1', 'uid2'], name='unique_friend')
        ]


class FriendApply(models.Model):
    """ 好友申请表 """
    STATUS = (
        (0, "申请中"),
        (1, "已接受"),
        (2, "已拒绝"),
    )
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    content = models.CharField(max_length=128)
    apply_time = models.DateTimeField(auto_now_add=True, db_index=True)
    status = models.SmallIntegerField(choices=STATUS)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['sender', 'receiver', 'apply_time'], name='unique_friend_apply')
        ]


class UserFavorStream(models.Model):
    """ 用户点赞动态记录表 """
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    sid = models.ForeignKey(Stream, on_delete=models.CASCADE, db_index=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['uid', 'sid'], name='unique_user_favor_stream')
        ]


# ----------------------------  辅助表  -------------------------------- #
class UserFavor(models.Model):
    """ 用户点赞过的活动类型 """
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=32)
    cnt = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['uid', 'category'], name='unique_user_favor')
        ]
