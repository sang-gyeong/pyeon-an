# Generated by Django 3.0.7 on 2020-06-25 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200625_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_youtuber',
            name='etc_require',
            field=models.TextField(null=True),
        ),
    ]
