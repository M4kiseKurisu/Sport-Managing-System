# Generated by Django 4.2.6 on 2023-10-28 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='pwd',
            new_name='password',
        ),
        migrations.AlterField(
            model_name='user',
            name='user_gender',
            field=models.SmallIntegerField(choices=[(0, '女'), (1, '男')]),
        ),
    ]
