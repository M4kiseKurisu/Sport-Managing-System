# Generated by Django 4.2.6 on 2023-12-02 20:45

import api.system.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_userfavor_userfavor_unique_user_favor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('sid', models.IntegerField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(max_length=512)),
                ('picture', models.ImageField(null=True, storage=api.system.storage.ImageStorage(), upload_to='images/stream/')),
                ('favor', models.IntegerField(default=0)),
                ('private', models.SmallIntegerField(choices=[(0, '仅自己可见'), (1, '好友可见'), (2, '所有人可见')])),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.activity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
        migrations.AddField(
            model_name='userinactivity',
            name='like',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='UserFavorStream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.stream')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('nid', models.IntegerField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(max_length=128)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
        migrations.AddConstraint(
            model_name='userfavorstream',
            constraint=models.UniqueConstraint(fields=('uid', 'sid'), name='unique_user_favor_stream'),
        ),
    ]
