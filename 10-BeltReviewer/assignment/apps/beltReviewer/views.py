# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect

from django.contrib import messages
from .models import User
 
def index(request):
    print "* index"
    errors = {}
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
    return render(request, "beltReviewer/index.html")

def registration(request):
    print "* registration"
    if request.method == "POST":
        errors = User.objects.registration_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')
        else:
            User.objects.create(first_name=request.POST.get('firstname'), last_name=request.POST.get('lastname'), email_address=request.POST.get('emailaddress'), password=request.POST.get('password1'))
            request.session['name'] = request.POST.get('firstname')
            return redirect('/books')
    return redirect('/')

def login(request):
    print "* login"
    temp_t = request.POST.get('email')
    temp_p = request.POST.get('password')
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')
        else:
            c1 = User.objects.filter(email_address=temp_t)
            if len(c1) > 0:
                c2 = User.objects.get(email_address=temp_t)
                if c2.password != temp_p:
                    errors["NotFound"] = "Email and Password should be match"
            else:
                errors["NotFound"] = "Email should be registed in our system"
            if len(errors):
                for tag, error in errors.iteritems():
                    messages.error(request, error, extra_tags=tag)
                return redirect('/')
            else:
                request.session['key'] = temp_t
                request.session['name'] = c2.first_name
                return redirect('/books')
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

def books(request):
    print "* books"
    if 'key' not in request.session:
        return redirect('/')
    context = {
        "all_users" : User.objects.all(),
        "name"      : request.session['name']
    }
    return render(request, "beltReviewer/books.html", context)