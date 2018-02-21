# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # authors = models.ManyToManyField(author, related_name="books")

    def __str__(self):
        return str(self.id)+'-'+self.name+'-'+self.desc+'-'+str(self.authors)

class author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    books = models.ManyToManyField(book, related_name="authors")
    notes = models.TextField(default='')

    def __str__(self):
        return str(self.id)+'-'+self.first_name+'-'+self.last_name+'-'+self.email+'-'+self.notes+'-'+str(self.books)