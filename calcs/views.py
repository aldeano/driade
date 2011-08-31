#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from django.shortcuts import render
from calcs.forms import ChillForm, HeatForm, EvapoForm

def home(request):
    return render(request, "calcs/calcs_index.html")
    
def chill(request):
    form = ChillForm()
    dicc = {"chill_form": form}
    return render(request, "calcs/chill.html", dicc)
    
def heat(request):
    form = HeatForm()
    dicc = {"heat_form": form}
    return render(request, "calcs/heat.html", dicc)
    
def evapo(request):
    form = EvapoForm()
    dicc = {"evapo_form": form}
    return render(request, "calcs/evapo.html", dicc)
    
