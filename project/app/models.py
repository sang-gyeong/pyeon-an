from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post_youtuber(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    datetime = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='youtuber')
    img = models.TextField(null=True)
    tool = models.TextField(null=True)
    name = models.TextField(null=True)
    work = models.TextField(null=True)
    career = models.TextField(null=True)
    period = models.TextField(null=True)
    style = models.TextField(null=True)
    genre = models.TextField(null=True)
    rating = models.TextField(null=True)
    vid_url = models.TextField(null=True)
    price = models.TextField(null=True)
    inquiry = models.TextField(null=True)
    etc_require = models.TextField(null=True)

    def __str__(self):
        return self.title

class Post_editor(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True)
    datetime = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='editor')
    name = models.TextField(null=True)
    img = models.TextField(null=True)
    tool = models.TextField(null=True)
    work = models.TextField(null=True)
    genre = models.TextField(null=True)
    style = models.TextField(null=True)
    rating = models.TextField(null=True)
    vid_url = models.TextField(null=True)
    basic_content = models.TextField(null=True)
    basic_price = models.TextField(null=True)
    standard_content = models.TextField(null=True)
    standard_price = models.TextField(null=True)
    premium_content = models.TextField(null=True)
    premium_price = models.TextField(null=True)
    inquiry = models.TextField(null=True)

    def __str__(self):
        return self.title

class Comment_youtuber(models.Model):
    post = models.ForeignKey(Post_youtuber, on_delete=models.CASCADE, related_name='comments_y')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_y')
    rate = models.IntegerField(default=5)
    datetime = models.TextField(null=True)

class Comment_editor(models.Model):
    post = models.ForeignKey(Post_editor, on_delete=models.CASCADE, related_name='comments_e')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_e')
    rate = models.IntegerField()
    datetime = models.TextField(null=True)

class Profile(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    name = models.TextField(null=True)
    gender = models.TextField(null=True)
    birth = models.TextField(null=True)
    phone = models.TextField(null=True)
    email = models.TextField(null=True)
   

