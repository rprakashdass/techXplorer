# Generated by Django 5.0.6 on 2024-06-09 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0002_user_userinfo_delete_followers_delete_likepost_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('dev', 'Developer'), ('student', 'Student')], default=None, max_length=10),
        ),
    ]
