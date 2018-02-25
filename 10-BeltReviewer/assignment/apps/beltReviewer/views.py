# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect

from django.contrib import messages
from .models import *
 
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
            c1 = User.objects.filter(email_address=request.POST.get('emailaddress'))
            if len(c1) > 0:
                errors["Found"] = "Email already in our system."
                for tag, error in errors.iteritems():
                    messages.error(request, error, extra_tags=tag)
                return redirect('/')
            ###
            User.objects.create(first_name=request.POST.get('firstname'), last_name=request.POST.get('lastname'), email_address=request.POST.get('emailaddress'), password=request.POST.get('password1'))
            ###
            c2 = User.objects.get(email_address=request.POST.get('emailaddress'))
            request.session['name'] = c2.first_name
            request.session['id'] = c2.id
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
                request.session['id'] = c2.id
                return redirect('/books')
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

def books(request):
    print "* books"
    if 'key' not in request.session:
        return redirect('/')
    b = Book.objects.all()
    r = Review.objects.all().order_by('-created_at')[:3]
    print r
    context = {
        "book_list"   : b,
        "review_list" : r,
        "name"        : request.session['name']
    }
    return render(request, "beltReviewer/books.html", context)

def add(request):
    print "* add"
    if 'key' not in request.session:
        return redirect('/')
    context = {
        "name"      : request.session['name']
    }
    return render(request, "beltReviewer/add.html", context)

def users(request, id):
    print "* users"
    if 'key' not in request.session:
        return redirect('/')
    r = Review.objects.filter(user=id)
    context = {
        "all_users"   : User.objects.filter(id=id),
        "all_reviews" : r,
        "cnt_reviews" : len(r),
        "name"        : request.session['name'],
    }
    print r
    return render(request, "beltReviewer/users.html", context)

def addbookreview(request):
    print "* addbookreview"
    if 'key' not in request.session:
        return redirect('/')
    errors = {}
    user=User.objects.get(id=request.session['id'])
    title = request.POST.get('title')
    if len(title) < 2:
        errors["title"] = "Title should be more than 2 characters"
    author_name = request.POST.get('author')
    if len(author_name) < 2:
        errors["author"] = "Author should be more than 2 characters"
    review = request.POST.get('review')
    if len(review) < 2:
        errors["review"] = "Review should be more than 2 characters"
    rating = request.POST.get('rating')
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('books/add')
    ###
    a = Author.objects.create(author_name=author_name)
    b = Book.objects.create(title=title,author=a)
    c = Review.objects.create(comment=review, book=b, rating=rating, user=user)
    return redirect('/books')

def bookdetails(request, id):
    print "* bookdetails"
    if 'key' not in request.session:
        return redirect('/')
    b = Book.objects.get(id=id)
    r = Review.objects.filter(book=b)
    request.session['book_id'] = b.id
    context = {
        "bookinfo"    : b,
        "all_reviews" : r,
        "name"        : request.session['name'],
    }
    return render(request, "beltReviewer/bookdetails.html", context)

def addreview(request):
    print "* addreview"
    if 'key' not in request.session:
        return redirect('/')
    errors = {}
    book_id = Book.objects.get(id=request.session['book_id'])
    user=User.objects.get(id=request.session['id'])
    review = request.POST.get('review')
    if len(review) < 2:
        errors["review"] = "Review should be more than 2 characters"
    rating = request.POST.get('rating')
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('books/add')
    ###
    c = Review.objects.create(comment=review, book=book_id, rating=rating, user=user)
    return redirect('/books')
