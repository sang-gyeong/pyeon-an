# Generated by Django 3.0.7 on 2020-06-13 07:16

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
            name='Post_youtuber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('datetime', models.DateTimeField()),
                ('img', models.TextField(null=True)),
                ('tool', models.TextField(null=True)),
                ('work', models.TextField(null=True)),
                ('career', models.TextField(null=True)),
                ('period', models.TextField(null=True)),
                ('style', models.TextField(null=True)),
                ('genre', models.TextField(null=True)),
                ('rating', models.TextField(null=True)),
                ('vid_url', models.TextField(null=True)),
                ('price', models.TextField(null=True)),
                ('inquiry', models.TextField(null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='youtuber', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post_editor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(null=True)),
                ('datetime', models.DateTimeField(null=True)),
                ('img', models.TextField(null=True)),
                ('tool', models.TextField(null=True)),
                ('work', models.TextField(null=True)),
                ('genre', models.TextField(null=True)),
                ('style', models.TextField(null=True)),
                ('rating', models.TextField(null=True)),
                ('vid_url', models.TextField(null=True)),
                ('basic_content', models.TextField(null=True)),
                ('basic_price', models.TextField(null=True)),
                ('standard_content', models.TextField(null=True)),
                ('standard_price', models.TextField(null=True)),
                ('premium_content', models.TextField(null=True)),
                ('premium_price', models.TextField(null=True)),
                ('inquiry', models.TextField(null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='editor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment_youtuber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('rate', models.IntegerField()),
                ('datetime', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_y', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_y', to='app.Post_youtuber')),
            ],
        ),
        migrations.CreateModel(
            name='Comment_editor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('rate', models.IntegerField()),
                ('datetime', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_e', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_e', to='app.Post_editor')),
            ],
        ),
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('datetime', models.DateTimeField()),
                ('reference', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apply', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]