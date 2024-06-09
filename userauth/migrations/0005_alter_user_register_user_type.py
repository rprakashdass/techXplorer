# Generated by Django 5.0.6 on 2024-06-09 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0004_rename_user_user_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_register',
            name='user_type',
            field=models.CharField(choices=[('test', 'test'), ('dev', 'Developer'), ('student', 'Student')], default=None, max_length=10),
        ),
    ]