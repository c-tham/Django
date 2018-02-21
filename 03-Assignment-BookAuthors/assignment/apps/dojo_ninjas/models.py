# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    desc = models.TextField(default="n/a")

    def __str__(self):
        return str(self.id)+'-'+self.name+'-'+self.city+'-'+self.state+'-'+self.desc

class ninjas(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    dojo = models.ForeignKey(dojos, related_name="ninjas")

    def __str__(self):
        return str(self.id)+'-'+self.first_name+'-'+self.last_name+'-'+str(self.dojo)
