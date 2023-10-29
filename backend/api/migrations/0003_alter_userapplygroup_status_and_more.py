# Generated by Django 4.2.6 on 2023-10-29 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_useringroup_manager_flag_userapplygroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userapplygroup',
            name='status',
            field=models.CharField(choices=[(1, '已接受'), (2, '已拒绝'), (0, '申请中')], max_length=8),
        ),
        migrations.AlterUniqueTogether(
            name='userapplygroup',
            unique_together={('uid', 'gid', 'apply_time')},
        ),
    ]
