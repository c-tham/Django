# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        if len(postData['firstname']) < 2:
            errors["firstname"] = "First name should be more than 2 characters"
        if len(postData['lastname']) < 2:
            errors["lastname"] = "Last name should be more than 2 characters"
        elif postData['lastname'].isalpha() == False:
            errors['lastname'] = "Last name should be all alpha characters"
        if len(postData['emailaddress']) < 7:
            errors["email"] = "Email address should be more than 7 characters"
        elif not EMAIL_REGEX.match(postData['emailaddress']):
            errors["email"] = "Email should be a valid email address"
        if len(postData['password1']) < 8:
            errors["password"] = "Password should be more than 8 characters"
        elif len(postData['password2']) < 8:
            errors["password"] = "Password should be more than 8 characters"
        if postData['password1'] != postData['password2']:
            errors["passwordNotMatch"] = "Password and confirm password should be matched"
        return errors
    
    def login_validator(self, postData):
        errors = {}
        if len(postData['email']) < 8:
            errors["email"] = "Login Email address should be more than 8 characters"
        elif not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Login Email should be a valid email address"
        if len(postData['password']) < 8:
            errors["password"] = "Login Password should be more than 8 characters"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    # birthday = models.DateTimeField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()
