#coding:utf-8
from django.shortcuts import render,render_to_response
import os
from django.http import HttpResponse
from django.template import RequestContext
from photo.models import *
# Create your views here.


def upload_photos(req):
    return render_to_response('index.html')

def receive(req):
    username=req.session["uname"]
    print username

    pic=req.FILES.get('pic')
    user=User.objects.get(uname=username)
    count=user.count
    user.count=count+1
    user.save()

    isexist=os.getcwd()+"/photo/static/"+username
    dir=os.getcwd()+"/photo/static/"+username+"/"+username+str(count)+".jpg"

    if os.path.exists(isexist):
        pass
    else:
        print "目录不存在,创建了目录"
        os.makedirs(isexist)
    file=open(dir,'w+')
    file.write(pic.read())
    file.close()
    pic=Pic.objects.create(pic=dir,user=user)
    pic.save()
    return render_to_response('main.html')

def show_photos(req):
    user=User.objects.get(uname=req.session["uname"])
    print user.uname
    pics=Pic.objects.filter(user=user)
    pic_list=list()
    for i in range(0,len(pics)):
        pi=list()

        pic=pics[i].pic
        pic=pic.replace(os.getcwd()+"/photo","")
        pi.append(pic)

        compent=list()
        qs = Comment.objects.filter(pic=pics[i])
        for i in qs:
            compent.append([i.user.uname,i.comment])
        pi.append(compent)
        pic_list.append(pi)
    print pic_list
    return render_to_response("show_photos.html",{"pic_list":pic_list})

def login(req):
    uname=req.GET["username"]
    passwd=req.GET["password"]
    req.session["123"]=uname
    try:
        user=User.objects.get(uname=uname)
        print user
        print user.passwd
        print passwd
        if(user.passwd==passwd):
            req.session["uname"] = uname
            return render_to_response("main.html")
        else:
            return HttpResponse("密码错误")
    except:
        return HttpResponse("用户不存在")

    return HttpResponse("123")

def register(req):
    uname = req.GET["username"]
    passwd = req.GET["password"]
    try:
        user=User.objects.get(uname=uname)
        return HttpResponse("用户名已存在")
    except:
        user=User()
        user.uname=uname
        user.passwd=passwd
        user.count=0
        user.save()
        return HttpResponse("创建成功")
def add_friend(req):
    uname=req.GET["friend_name"]
    friend=User.objects.get(uname=uname)
    user=User.objects.get(uname=req.session["uname"])

    user.firends.add(friend)
    user.save()

    friend.firends.add(user)
    friend.save()

    return HttpResponse("ok")
def delete_friend(req):
    uname = req.GET["friend_name"]
    friend = User.objects.get(uname=uname)
    user = User.objects.get(uname=req.session["uname"])

    user.firends.remove(friend)
    user.save()

    friend.firends.remove(user)
    friend.save()
    return HttpResponse("ok")
def friend_list(req):
    user = User.objects.get(uname=req.session["uname"])
    friends=list(user.firends.all())
    frds=list()
    for f in friends:
        friend={}
        friend["uname"]=f.uname
        frds.append(friend)
    return render_to_response("friends_list.html",{"friends":frds})
def comment_photo(req):
    user=User.objects.get(uname=req.session["uname"])

    pic=req.GET["pic"]
    pic=Pic.objects.get(pic=pic)
    comment=req.GET["comment"]

    qs=Comment.objects.filter(pic=pic)

    if len(list(qs))==0:
        c=Comment()
        c.pic=pic
        c.user=user
        c.comment=comment
        c.save()
    else:
        count=qs[len(qs)-1].count
        c = Comment()
        c.pic = pic
        c.user = user
        c.comment = comment
        c.count=count+1
        c.save()



    return HttpResponse("ok")
