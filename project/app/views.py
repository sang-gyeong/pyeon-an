from django.shortcuts import render, redirect
from .models import Post_youtuber, Post_editor, Comment_editor, Comment_youtuber, Profile
from django.contrib.auth.models import User 
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from datetime import datetime
from project.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME, AWS_S3_FILE_OVERWRITE
import boto3
from boto3.session import Session

# Create your views here.
def home(request):
    comment_editor = Comment_editor.objects.all()
    post_editor = Post_editor.objects.all()
    post_youtuber = Post_youtuber.objects.all()
    return render(request, 'home.html', {'comment_editor' : comment_editor, 'post_editor' : post_editor, 'post_youtuber' : post_youtuber})


def list_editor(request):
    post_editor = Post_editor.objects.all()
    return render(request, 'list_editor.html', {'post_editor' : post_editor})

def list_youtuber(request):
    post_youtuber = Post_youtuber.objects.all()
    return render(request, 'list_youtuber.html', {'post_youtuber' : post_youtuber})


def delete_editor(request, post_pk):
    post_editor = Post_editor.objects.get(pk=post_pk)
    post_editor.delete()
    return redirect('list_editor')

def delete_youtuber(request, post_pk):
    post_youtuber = Post_youtuber.objects.get(pk=post_pk)
    post_youtuber.delete()
    return redirect('list_youtuber')


@login_required(login_url='/registration/login')
def detail_editor(request, post_pk):
    post = Post_editor.objects.get(pk=post_pk)
    if request.method == "POST":
        Comment_editor.objects.create(
           post = post,
           content = request.POST['content'],
           author = request.user,
           rate = request.POST['rate'],
           datetime = datetime.now().strftime('%Y/%m/%d %H:%M')
        )
        return redirect('detail_editor', post_pk)
    return render(request, 'detail_editor.html', {'post' : post})

def delete_comment_e(request, post_pk, comment_pk):
    comment = Comment_editor.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail_editor', post_pk)

def delete_comment_y(request, post_pk, comment_pk):
    comment = Comment_youtuber.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail_youtuber', post_pk)

@login_required(login_url='/registration/login')
def detail_youtuber(request, post_pk):
    post = Post_youtuber.objects.get(pk=post_pk)

    if request.method == "POST":
        Comment_youtuber.objects.create(
           post = post,
           content = request.POST['content'],
           author = request.user,
           rate = request.POST['rate'],
           datetime = datetime.now().strftime('%Y/%m/%d %H:%M')
        )
        return redirect('detail_youtuber', post_pk)
    return render(request, 'detail_youtuber.html', {'post' : post})

@login_required(login_url='/registration/login')
def form_to_editor(request):
    if (request.method == 'POST'):
        Apply.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            author = request.user,
            datetime = datetime.now(),
            reference = request.POST['reference']
        )
        return redirect(request, 'detail_editor')
    return render(request, 'form_to_editor.html')

@login_required(login_url='/registration/login')
def form_to_youtuber(request):
    if (request.method == 'POST'):
        Apply.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            author = request.user,
            datetime = datetime.now(),
            reference = request.POST['reference']
        )
        return redirect(request, 'detail_youtuber')
    return render(request, 'form_to_youtuber.html')

@login_required(login_url='/registration/login')
def new_editor(request):
    if (request.method == 'POST'):
        file_to_upload = request.FILES.get("img")
        session = Session(
        aws_access_key_id = AWS_ACCESS_KEY_ID,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
        region_name = AWS_S3_REGION_NAME
        )
        s3 = session.resource("s3")
        now = datetime.now().strftime("%Y%H%M%S")

        img_object = s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
            Key = now + file_to_upload.name,
            Body = file_to_upload
        )
        s3_url = 'https://sanggyeong-bucket.s3.ap-northeast-2.amazonaws.com/'

        url_arr = request.POST['vid_url'].split('=')

        new_post = Post_editor.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            author = request.user,
            name = request.POST['name'],
            datetime = datetime.now(),   
            tool = request.POST['tool'],
            work =request.POST['work'],
            style = request.POST['style'],
            genre = request.POST['genre'],
            basic_content = request.POST['basic_content'],
            basic_price = request.POST['basic_price'],
            standard_content = request.POST['standard_content'],
            standard_price = request.POST['standard_price'],
            premium_content = request.POST['premium_content'],
            premium_price = request.POST['premium_price'],
            vid_url = 'https://www.youtube.com/embed/' + url_arr[1],
            inquiry=request.POST['inquiry'],
            img = s3_url + now + file_to_upload.name
        )
        return redirect('detail_editor', new_post.pk)
    return render(request, 'new_editor.html')

@login_required(login_url='/registration/login')
def new_youtuber(request):
    if (request.method == 'POST'):
        file_to_upload = request.FILES.get('img')
        session = Session(
        aws_access_key_id = AWS_ACCESS_KEY_ID,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
        region_name = AWS_S3_REGION_NAME
        )
        s3 = session.resource("s3")
        now = datetime.now().strftime("%Y%H%M%S")

        img_object = s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
            Key = now + file_to_upload.name,
            Body = file_to_upload
        )
        s3_url = 'https://sanggyeong-bucket.s3.ap-northeast-2.amazonaws.com/'

        url_arr = request.POST['vid_url'].split('=')
        
        new_post = Post_youtuber.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            author = request.user,
            name = request.POST['name'],
            datetime = datetime.now(),   
            tool = request.POST['tool'],
            genre = request.POST['genre'],
            work =request.POST['work'],
            career = request.POST['career'],
            period = request.POST['period'],
            vid_url = 'https://www.youtube.com/embed/' + url_arr[1],
            img = s3_url + now + file_to_upload.name,
            etc_require = requiest.POST['etc_require']
        )
        return redirect('detail_youtuber', new_post.pk)

    return render(request, 'new_youtuber.html')

@login_required(login_url='/registration/login')
def edit_editor(request, post_pk):
    post = Post_editor.objects.get(pk=post_pk)
    
    if (request.method == 'POST'):
        file_to_upload = request.FILES.get("img")
        session = Session(
        aws_access_key_id = AWS_ACCESS_KEY_ID,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
        region_name = AWS_S3_REGION_NAME
        )
        s3 = session.resource("s3")
        now = datetime.now().strftime("%Y%H%M%S")

        img_object = s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
            Key = now + file_to_upload.name,
            Body = file_to_upload
        )
        s3_url = 'https://sanggyeong-bucket.s3.ap-northeast-2.amazonaws.com/'

        Post_editor.objects.filter(pk=post_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            author = request.user,
            datetime = datetime.now(),   
            tool = request.POST['tool'],
            work =request.POST['work'],
            career = request.POST['career'],
            img = s3_url + now + file_to_upload.name
        )
        return redirect('detail_editor', post_pk)
    return render(request, 'edit_editor.html', {'post' : post})
        
@login_required(login_url='/registration/login')
def edit_youtuber(request, post_pk):
    post = Post_youtuber.objects.get(pk=post_pk)
    
    if (request.method == 'POST'):
        file_to_upload = request.FILES.get("img")
        session = Session(
        aws_access_key_id = AWS_ACCESS_KEY_ID,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
        region_name = AWS_S3_REGION_NAME
        )
        s3 = session.resource("s3")
        now = datetime.now().strftime("%Y%H%M%S")

        img_object = s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
            Key = now + file_to_upload.name,
            Body = file_to_upload
        )
        s3_url = 'https://sanggyeong-bucket.s3.ap-northeast-2.amazonaws.com/'


        Post_youtuber.objects.filter(pk=post_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            author = request.user,
            datetime = datetime.now(),   
            tool = request.POST['tool'],
            work =request.POST['work'],
            career = request.POST['career'],
            period = request.POST['period'],
            genre = request.POST['genre'],
            rating = request.POST['rating'],
            img = s3_url + now + file_to_upload.name,
            etc_require = requiest.POST['etc_require']
        )
        return redirect('detail_youtuber', post_pk)
    return render(request, 'edit_youtuber.html', {'post' : post})

@login_required(login_url='/registration/login')
def mypage_youtuber(request):
    return render(request, 'mypage_youtuber.html')

@login_required(login_url='/registration/login')
def mypage_editor(request):
    return render(request, 'mypage_editor.html')

def signup(request):
    if request.method == "POST":
        found_user = User.objects.filter(username=request.POST['username'])
        if len(found_user) > 0:
            error = "아이디가 이미 존재합니다."
            return render(request, 'registration/signup.html', {'error' : error})

        new_user = User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password']
        )
        auth.login(request, new_user)
        return redirect('home')
    
    return render(request, 'registration/signup.html')


def login(request):
    if request.method == "POST":
        found_user = auth.authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if found_user is None:
            error = "아이디 또는 비밀번호가 틀렸습니다."
            return render(request, 'registration/login.html', {'error' : error})

        auth.login(request, found_user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect(request.GET.get('next','/'))
    
    return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def payment(request):
    return render(request, 'payment.html')

def mypage_apply(request):
    return render(request, 'mypage_apply.html')

def mypage_contract(request):
    return render(request, 'mypage_contract.html')

def mypage_pay(request):
    return render(request, 'mypage_pay.html')

def index(request):
    return render(request, 'chat/index.html')

@login_required(login_url='/registration/login')
def profile(request):
    # profile = Profile.objects.get(pk=user_pk)
    return render(request, 'profile.html')

def profile_edit(request):
    # profile = Profile.objects.get(pk=user_pk)
    return render(request, 'profile_edit.html')
