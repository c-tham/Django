# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
 
def index(request):
    context = {
        "name" : "courses"
    }
    return render(request, "courses/index.html", context)
