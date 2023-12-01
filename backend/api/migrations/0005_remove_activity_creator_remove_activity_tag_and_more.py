# Generated by Django 4.2.6 on 2023-11-25 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_userapplygroup_status_alter_useringroup_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='usercreateactivity',
            name='private',
        ),
        migrations.AddField(
            model_name='activity',
            name='favor',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activity',
            name='private',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activity',
            name='tags',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activity',
            name='type',
            field=models.SmallIntegerField(choices=[(1, '团体'), (0, '个人')], default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='capacity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='friendapply',
            name='status',
            field=models.SmallIntegerField(choices=[(1, '已接受'), (2, '已拒绝'), (0, '申请中')]),
        ),
        migrations.AlterField(
            model_name='group',
            name='capacity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='groupequipment',
            name='is_return',
            field=models.SmallIntegerField(choices=[(0, '未归还'), (2, '已归还')], default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_gender',
            field=models.SmallIntegerField(choices=[(0, '女'), (1, '男')]),
        ),
        migrations.AlterField(
            model_name='userapplygroup',
            name='status',
            field=models.SmallIntegerField(choices=[(1, '已接受'), (2, '已拒绝'), (0, '申请中')]),
        ),
        migrations.AlterField(
            model_name='userequipment',
            name='is_return',
            field=models.SmallIntegerField(choices=[(0, '未归还'), (2, '已归还')], default=0),
        ),
        migrations.AlterField(
            model_name='useringroup',
            name='type',
            field=models.SmallIntegerField(choices=[(0, '创建人'), (1, '管理员'), (2, '成员')]),
        ),
    ]
