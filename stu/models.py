# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
    sname=models.CharField(max_length=30,unique=True)
    spwd=models.CharField(max_length=30)



class Category(models.Model):
    cname = models.CharField(max_length=30)

class Clazz(models.Model):
    cno = models.AutoField(primary_key=True)