# Generated by Django 4.0.1 on 2022-12-26 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0002_goal_goalcomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goal',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='goalcomment',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='goalcomment',
            name='title',
        ),
    ]
