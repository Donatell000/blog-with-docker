# Generated by Django 4.2.16 on 2024-10-18 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_rename_user_profile_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_id',
            new_name='user',
        ),
    ]
