# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 5:
            errors["firstname"] = "First name should be more than 5 characters"
        if len(postData['last_name']) < 5:
            errors["lastname"] = "Last name should be more than 5 characters"
        if len(postData['email_address']) < 5:
            errors["email"] = "Email address should be more than 5 characters"
        elif not EMAIL_REGEX.match(postData['email_address']):
            errors["email"] = "Email should be a valid email address"
        return errors

class user(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()