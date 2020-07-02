"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('list_youtuber/', views.list_youtuber, name="list_youtuber"),
    path('list_editor/', views.list_editor, name="list_editor"),
    path('detail_youtuber/<int:post_pk>', views.detail_youtuber, name="detail_youtuber"),
    path('detail_editor/<int:post_pk>', views.detail_editor, name="detail_editor"),
    path('new_youtuber/', views.new_youtuber, name="new_youtuber"),
    path('new_editor/', views.new_editor, name="new_editor"),
    path('delete_editor/<int:post_pk>', views.delete_editor, name="delete_editor"),
    path('delete_youtuber/<int:post_pk>', views.delete_youtuber, name="delete_youtuber"),
   
    path('edit_youtuber/<int:post_pk>', views.edit_youtuber, name="edit_youtuber"),
    path('edit_editor/<int:post_pk>', views.edit_editor, name="edit_editor"),
    path('mypage_youtuber', views.mypage_youtuber, name="mypage_youtuber"),
    path('mypage_editor', views.mypage_editor, name="mypage_editor"),
    path('mypage_apply/<int:user_pk>', views.mypage_apply, name="mypage_apply"),
    path('mypage_contract/<int:user_pk>', views.mypage_contract, name="mypage_contract"),
    path('mypage_pay/<int:user_pk>', views.mypage_pay, name="mypage_pay"),
    path('payment/', views.payment, name="payment"),
    path('form_to_youtuber/', views.form_to_youtuber, name="form_to_youtuber"),
    path('form_to_editor/', views.form_to_editor, name="form_to_editor"),
    path('registration/signup', views.signup, name="signup"),
    path('registration/login', views.login, name="login"),
    path('registration/logout', views.logout, name="logout"),
    path('delete_comment_e/<int:post_pk>/<int:comment_pk>', views.delete_comment_e, name="delete_comment_e"),
    path('delete_comment_y/<int:post_pk>/<int:comment_pk>', views.delete_comment_y, name="delete_comment_y"),
    path('profile', views.profile, name="profile"),
    path('profile_edit', views.profile_edit, name="profile_edit"),

]
