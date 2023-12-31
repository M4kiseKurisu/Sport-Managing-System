# Generated by Django 4.2.6 on 2023-12-01 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_activity_category_groupcreateactivity_uid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFavor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=32)),
                ('cnt', models.IntegerField()),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
        migrations.AddConstraint(
            model_name='userfavor',
            constraint=models.UniqueConstraint(fields=('uid', 'category'), name='unique_user_favor'),
        ),
    ]
