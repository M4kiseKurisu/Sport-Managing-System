# Generated by Django 4.2.6 on 2023-11-27 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_activity_type_alter_friendapply_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='category',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='groupcreateactivity',
            name='uid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activityusefield',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='activityusefield',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]