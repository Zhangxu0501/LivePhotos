#coding:utf-8
from django.shortcuts import render,render_to_response
import os
from django.http import HttpResponse
from django.template import RequestContext
from photo.models import User,Pic
# Create your views here.


def upload_photos(req):
    return render_to_response('upload_photos.html')

def receive(req):
    username="fanzhen"
    pic=req.FILES.get('pic')
    user=User.objects.get(uname=username)
    count=user.count
    user.count=count+1
    user.save()

    dir=os.getcwd()+"/photo/static/"+username+"/"+username+str(count)+".jpg"
    print dir
    file=open(dir,'w+')
    file.write(pic.read())
    file.close()

    user.count = count + 1
    user.save()
    pic=Pic.objects.create(pic=dir,user=user)
    pic.save()


    return render_to_response('upload_photos.html')

def show_photos(req):

    user=User.objects.get(uname="fanzhen")
    pics=Pic.objects.filter(user=user)

    pic_list=list()
    a=list()
    for i in range(0,len(pics)):
        pic=pics[i].pic
        pic=pic.replace("/Users/zhangxu/PycharmProjects/LivePhotos/photo","")
        if i%2==1:
            a.append(pic)
            pic_list.append(a)
            a=list()
        a.append(pic)
    return render_to_response("show_photos.html",{"pic_list":pic_list})
