# Generated by Django 3.0.7 on 2020-06-26 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth',
            field=models.TextField(default='입력 없음', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.TextField(default='입력 없음', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.TextField(default='입력 없음', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.TextField(default='입력 없음', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.TextField(default='입력 없음', null=True),
        ),
    ]
