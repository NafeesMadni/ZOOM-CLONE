# Generated by Django 5.1.2 on 2024-10-24 10:56

import authentication.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='acc_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='dp',
            field=models.ImageField(default=authentication.models.get_default_image_path, upload_to='user_dp/'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='nickname',
            field=models.CharField(default='James Doe', max_length=15),
        ),
    ]