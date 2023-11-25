# Generated by Django 4.2.6 on 2023-11-24 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_activity_capacity_activity_creator_activity_tag_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userapplygroup',
            name='status',
            field=models.SmallIntegerField(choices=[(0, '申请中'), (2, '已拒绝'), (1, '已接受')]),
        ),
        migrations.AlterField(
            model_name='useringroup',
            name='type',
            field=models.SmallIntegerField(choices=[(1, '管理员'), (2, '成员'), (0, '创建人')]),
        ),
        migrations.CreateModel(
            name='FriendApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=128)),
                ('apply_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.SmallIntegerField(choices=[(0, '申请中'), (2, '已拒绝'), (1, '已接受')])),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='api.user')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='api.user')),
            ],
        ),
        migrations.AddConstraint(
            model_name='friendapply',
            constraint=models.UniqueConstraint(fields=('sender', 'receiver', 'apply_time'), name='unique_friend_apply'),
        ),
    ]