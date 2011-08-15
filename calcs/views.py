#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from django.shortcuts import render

def home(request):
    return render(request, "calcs/index.html")
    
def chill(request):
    pass
    
def heat(request):
    pass
    
def evapo(request):
    pass
    
