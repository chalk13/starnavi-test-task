# Generated by Django 2.2 on 2020-01-25 19:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_auto_20200125_1904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='post_liked',
            new_name='post_like',
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('user', 'post', 'post_like')},
        ),
    ]