# Generated by Django 4.2.6 on 2023-12-11 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_stream_userinactivity_like_userfavorstream_notice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='category',
            field=models.CharField(db_index=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='activity',
            name='name',
            field=models.CharField(db_index=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='activity',
            name='type',
            field=models.SmallIntegerField(choices=[(0, '个人'), (1, '团体')], db_index=True),
        ),
        migrations.AlterField(
            model_name='activityusefield',
            name='end_time',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='activityusefield',
            name='start_time',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='category',
            field=models.CharField(db_index=True, max_length=16),
        ),
        migrations.AlterField(
            model_name='friendapply',
            name='apply_time',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='time',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='stream',
            name='time',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='userapplygroup',
            name='apply_time',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
