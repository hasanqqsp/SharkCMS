# Generated by Django 3.2.3 on 2021-05-17 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='user_uploads/')),
                ('is_writer', models.BooleanField(default=True)),
                ('is_trusted_writer', models.BooleanField(default=False)),
                ('is_moderator', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_disabled', models.BooleanField(default=False)),
                ('is_muted', models.BooleanField(default=False)),
                ('bio', models.TextField(blank=True, null=True)),
                ('short_bio', models.CharField(blank=True, max_length=256, null=True)),
                ('registered', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
