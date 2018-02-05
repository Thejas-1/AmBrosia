# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
    index = models.AutoField(primary_key=True)
    food1 = "food1"
    food2 = "food2"
    food3 = "food3"
