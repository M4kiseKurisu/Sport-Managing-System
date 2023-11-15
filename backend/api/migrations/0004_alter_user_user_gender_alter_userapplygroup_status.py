# Generated by Django 4.2.6 on 2023-11-10 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_groupequipment_is_return_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_gender',
            field=models.SmallIntegerField(choices=[(0, '女'), (1, '男')]),
        ),
        migrations.AlterField(
            model_name='userapplygroup',
            name='status',
            field=models.SmallIntegerField(choices=[(2, '已拒绝'), (1, '已接受'), (0, '申请中')]),
        ),
    ]