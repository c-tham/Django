# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect

from django.contrib import messages
from .models import User
 
def index(request):
    print "* index"
    return render(request, "login_registration/index.html")

def registration(request):
    print "* registration"
    if request.method == "POST":
        User.objects.create(first_name=request.POST.get('firstname'), last_name=request.POST.get('lastname'), email_address=request.POST.get('emailaddress'), password=request.POST.get('password1'))
        return redirect('/login')
    return redirect('/')

def login(request):
    print "* login"
    context = {
        "all_users" : User.objects.all(),
        "name"      : request.POST.get('firstname')
    }
    return render(request, "login_registration/dashboard.html", context)
    return redirect('/')
