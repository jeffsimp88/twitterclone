# Generated by Django 3.1.7 on 2021-03-02 17:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitteruser', '0002_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followers',
            name='following_user',
            field=models.ManyToManyField(blank=True, null=True, related_name='following_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
