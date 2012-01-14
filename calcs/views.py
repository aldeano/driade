#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from django import forms
from django.shortcuts import render
from django.http import HttpResponse, Http404
from calcs.forms import ChillForm, HeatForm, EvapoForm, heat_choices, chill_choices
from calcs.algoritms import *
   
def phenology(request, purpose=None):
    
    #check for a real purpose
    potential_purposes = ["Chill", "Heat", "Evapo"]
    if purpose not in potential_purposes:
        raise Http404
        
    results = None
    #create string to call proper form
    string_to_call = purpose + "Form"
    #call form using the string
    mod = __import__("calcs.forms", fromlist=[string_to_call])
    form = getattr(mod, string_to_call)
    form_url = "/calcs/" + purpose + "/"
    #search for the first explanation of each purpose
    #and separate evapo forms from the others
    if purpose == "Chill":
        explanation = explanations["horas_frio"]
        choices_field = True
    elif purpose == "Heat":
        explanation = explanations["dias_grado"]
        choices_field = True
    else:
        explanation = explanations["evapotranspiracion"]
        choices_field = False
        
    if request.method == "POST":
        form = getattr(mod, string_to_call)(request.POST)
        if form.is_valid():
            phenologic_calc = purpose
            results = algoritms(phenologic_calc, form.cleaned_data)
            results = str(results) + " " + units[form.cleaned_data["chosen_method"]]
            string_choice = purpose.lower() + "_choices"
            form = getattr(mod, string_to_call)(initial={'chosen_method': eval(string_choice)[0][0]})

    dicc = {"form": form, "form_url": form_url, "results": results,
    "explanation": explanation}
    
    return render(request, "calcs/calcs_index.html", dicc)

def ajax_expl(request, method):
    #Choose the correct explanation for each method through ajax request.
    if request.is_ajax():
        explanation = explanations[method]
    return HttpResponse(explanation)
