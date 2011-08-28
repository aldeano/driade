#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from django.shortcuts import render

def home(request):
    return render(request, "calcs/calcs_index.html")
    
def chill(request):
    return render(request, "calcs/chill.html")
    
def heat(request):
    return render(request, "calcs/heat.html")
    
def evapo(request):
    return render(request, "calcs/evapo.html")
    
