"""LivePhotos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from photo.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',upload_photos),
    url(r'receive',receive),
    url(r'show_photos',show_photos),
    url(r'login',login),
    url(r'register',register),
    url(r'add_friend',add_friend),
    url(r"delete_friend",delete_friend),
    url(r'friend_list',friend_list),
    url(r'comment_photo',comment_photo)

]
