# Generated by Django 3.2.5 on 2021-07-14 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='created_date',
        ),
        migrations.AddField(
            model_name='video',
            name='video_url',
            field=models.URLField(null=True),
        ),
    ]
