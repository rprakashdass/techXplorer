# Generated by Django 5.0.6 on 2024-06-09 15:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0005_alter_user_register_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_register',
            name='user_type',
            field=models.CharField(choices=[('test', 'Test'), ('dev', 'Developer'), ('student', 'Student')], default=None, max_length=10),
        ),
        migrations.CreateModel(
            name='Aideed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=255)),
                ('posted_location', models.CharField(max_length=255)),
                ('posted_support', models.CharField(max_length=255)),
                ('queries', models.TextField()),
                ('demo_link', models.URLField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aideed_posts', to='userauth.user_register')),
            ],
        ),
        migrations.CreateModel(
            name='Apisfeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=255)),
                ('posted_location', models.CharField(max_length=255)),
                ('posted_support', models.CharField(max_length=255)),
                ('queries', models.TextField()),
                ('demo_link', models.URLField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apis_posts', to='userauth.user_register')),
            ],
        ),
        migrations.CreateModel(
            name='Hackathonsfeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=255)),
                ('posted_location', models.CharField(max_length=255)),
                ('posted_support', models.CharField(max_length=255)),
                ('queries', models.TextField()),
                ('demo_link', models.URLField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hackathons_posts', to='userauth.user_register')),
            ],
        ),
        migrations.CreateModel(
            name='JobPostings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=255)),
                ('posted_location', models.CharField(max_length=255)),
                ('posted_support', models.CharField(max_length=255)),
                ('queries', models.TextField()),
                ('demo_link', models.URLField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_posts', to='userauth.user_register')),
            ],
        ),
    ]
