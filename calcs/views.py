#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from django import forms
from django.shortcuts import render
from calcs.forms import ChillForm, HeatForm, EvapoForm, heat_choices, chill_choices
from calcs.algoritms import *
   
def phenology(request, purpose=None):
    
    results = None
    #create string to call proper form
    string_to_call = purpose + "Form"
    #call form using the string
    mod = __import__("calcs.forms", fromlist=[string_to_call])
    form = getattr(mod, string_to_call)
    form_url = "/calcs/" + purpose + "/"
    
    if request.method == "POST":
        form = getattr(mod, string_to_call)(request.POST)
        if form.is_valid():
            phenologic_calc = purpose
            results = algoritms(phenologic_calc, form.cleaned_data)
            results = str(results) + " " + units[form.cleaned_data["chosen_method"]]
    
    dicc = {"form": form, "form_url": form_url, "results": results}
    
    return render(request, "calcs/calcs_index.html", dicc)
