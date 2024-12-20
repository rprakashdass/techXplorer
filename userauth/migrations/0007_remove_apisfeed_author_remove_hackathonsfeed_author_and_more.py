# Generated by Django 5.0.6 on 2024-06-09 15:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0006_alter_user_register_user_type_aideed_apisfeed_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apisfeed',
            name='author',
        ),
        migrations.RemoveField(
            model_name='hackathonsfeed',
            name='author',
        ),
        migrations.RemoveField(
            model_name='jobpostings',
            name='author',
        ),
        migrations.CreateModel(
            name='AiModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=255)),
                ('posted_location', models.CharField(max_length=255)),
                ('posted_support', models.CharField(max_length=255)),
                ('queries', models.TextField()),
                ('demo_link', models.URLField(blank=True, null=True)),
                ('post_image', models.ImageField(blank=True, null=True, upload_to='hackathon_images/')),
                ('post_video', models.FileField(blank=True, null=True, upload_to='hackathon_videos/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userauth.user_register')),
            ],
        ),
        migrations.CreateModel(
            name='ExploreApi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=255)),
                ('posted_location', models.CharField(max_length=255)),
                ('posted_support', models.CharField(max_length=255)),
                ('queries', models.TextField()),
                ('demo_link', models.URLField(blank=True, null=True)),
                ('post_image', models.ImageField(blank=True, null=True, upload_to='hackathon_images/')),
                ('post_video', models.FileField(blank=True, null=True, upload_to='hackathon_videos/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userauth.user_register')),
            ],
        ),
        migrations.CreateModel(
            name='Hackathons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=255)),
                ('posted_location', models.CharField(max_length=255)),
                ('posted_support', models.CharField(max_length=255)),
                ('queries', models.TextField()),
                ('demo_link', models.URLField(blank=True, null=True)),
                ('post_image', models.ImageField(blank=True, null=True, upload_to='hackathon_images/')),
                ('post_video', models.FileField(blank=True, null=True, upload_to='hackathon_videos/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userauth.user_register')),
            ],
        ),
        migrations.DeleteModel(
            name='Aideed',
        ),
        migrations.DeleteModel(
            name='Apisfeed',
        ),
        migrations.DeleteModel(
            name='Hackathonsfeed',
        ),
        migrations.DeleteModel(
            name='JobPostings',
        ),
    ]
