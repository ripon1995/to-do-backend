# Generated by Django 4.1.7 on 2023-07-14 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_user_first_name_user_last_name_alter_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]