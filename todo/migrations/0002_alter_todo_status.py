# Generated by Django 4.1.7 on 2023-03-06 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('NEW', 'New Task'), ('RUNNING', 'Running Task'), ('FUTURE', 'Future Task')], default='NEW', max_length=20),
        ),
    ]
