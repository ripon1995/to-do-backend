# Generated by Django 4.1.7 on 2023-07-10 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_groups_user_is_superuser_user_last_login_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='device_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
