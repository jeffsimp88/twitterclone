# Generated by Django 3.1.7 on 2021-03-03 13:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitteruser', '0003_auto_20210302_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='following_user',
            field=models.ManyToManyField(blank=True, related_name='users_following', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Followers',
        ),
    ]
