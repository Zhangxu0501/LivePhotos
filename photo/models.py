from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    uname=models.CharField(max_length=30,null=False)
    passwd=models.CharField(max_length=30,null=False)
    count=models.IntegerField()

class Pic(models.Model):
    pic=models.CharField(max_length=30)
    user=models.ForeignKey(User)


