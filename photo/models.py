from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    uname=models.CharField(max_length=30,null=False)
    passwd=models.CharField(max_length=30,null=False)
    count=models.IntegerField()
    firends=models.ManyToManyField("self")



class Pic(models.Model):
    pic=models.CharField(max_length=30)
    user=models.ForeignKey(User)


class Comment(models.Model):
    count=models.IntegerField(default=1,auto_created=True)
    comment=models.CharField(max_length=300,null=True)
    pic=models.ForeignKey(Pic)
    user=models.ForeignKey(User)



