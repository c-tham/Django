# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import user

def index(request):
    return redirect('/users')

def users(request):
    print 'show all users page'
    context = {
        "all_users" : user.objects.all(),
        "key" : 0
    }
    return render(request, "crud/index.html", context)

def new(request):
    print 'show insert page'
    return render(request, "crud/new.html")

def create(request):
    print 'insert a record'
    if request.method == "POST":
        errors = user.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/users/new')
        else:
            user.objects.create(first_name=request.POST.get('first_name'), last_name=request.POST.get('last_name'), email_address=request.POST.get('email_address'))
    return redirect('/users')

def show(request, row):
    print 'show a user page'
    context = {
        "all_users" : user.objects.filter(id=row),
        "key" : 1
    }
    return render(request, "crud/index.html", context)

def edit(request, row):
    print 'edit a user page'
    context = {
        # "all_users" : user.objects.filter(id=row).values()
        "all_users" : user.objects.get(id=row)
    }
    return render(request, "crud/edit.html", context)

def update(request):
    print 'update a user page'
    if request.method == "POST":
        r = request.POST.get('row')
        errors = user.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/users/'+r+'/edit')
        else:
            print request.POST
            print '  save it'
            u = user.objects.get(id=r)
            u.first_name = request.POST.get('first_name')
            u.last_name = request.POST.get('last_name')
            u.email_address = request.POST.get('email_address')
            u.save()
            print '  diplay it'
            context = {
                "all_users" : user.objects.filter(id=r),
                "key" : 1
            }
            return render(request, "crud/index.html", context)
    return redirect('/users')

def delete(request, row):
    print 'delete a user'
    u = user.objects.get(id=row)
    u.delete()
    return redirect('/users')