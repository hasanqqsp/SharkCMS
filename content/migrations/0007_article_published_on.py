# Generated by Django 3.2.3 on 2021-05-19 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_auto_20210519_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='published_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]