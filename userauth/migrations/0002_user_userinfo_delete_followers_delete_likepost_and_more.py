# Generated by Django 5.0.6 on 2024-06-09 11:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('user_type', models.CharField(choices=[('dev', 'Developer'), ('student', 'Student')], max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('company', models.CharField(blank=True, max_length=255, null=True)),
                ('experience', models.CharField(blank=True, max_length=255, null=True)),
                ('job_title', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('domain', models.CharField(blank=True, max_length=255, null=True)),
                ('institute', models.CharField(blank=True, max_length=255, null=True)),
                ('branch', models.CharField(blank=True, max_length=255, null=True)),
                ('interested_domains', models.CharField(blank=True, max_length=255, null=True)),
                ('interested_domains_to_follow', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='info', to='userauth.user')),
            ],
        ),
        migrations.DeleteModel(
            name='Followers',
        ),
        migrations.DeleteModel(
            name='LikePost',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
