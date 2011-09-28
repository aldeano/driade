#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from django.shortcuts import render
from calcs.forms import *

def home(request):
    
    chill_form = ChillForm()
    heat_form = HeatForm()
    evapo_form = EvapoForm()
    dicc = {"chill_form": chill_form, "heat_form": heat_form, 
    "evapo_form": evapo_form,}
    
    return render(request, "index.html", dicc)
