#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from django import forms
from django.shortcuts import render
from django.http import HttpResponse, Http404
from calcs.forms import *
from calcs.algoritms import *
   
def phenology(request, purpose=None):
    
    results = None
    #check for a real purpose
    potential_purposes = ["chill", "heat", "evapo"]
    if purpose not in potential_purposes:
        raise Http404
    #asign choices for each purpose, respective form and explanation    
    if purpose == "chill":
        choices = chill_choices
        form = tempForm
        explanation = explanations['horas_frio']
    elif purpose == "heat":
        choices = heat_choices
        form = tempForm
        explanation = explanations['dias_grado']
    else:
        choices = evapo_choices
        form = evapoForm
        explanation = explanations['penman_monteith_fao']
    
    form_choices = choicesForm(method=choices)
    form_url = "/calcs/" + purpose + "/"
        
    if request.method == "POST":
        form = form(request.POST)
        form_choices = form_choices(request.POST)
        if form.is_valid() and form_choices.is_valid():
            #join both post form datas
            formData = dict(form.items() + form_choices.items())
            results = algoritms(purpose, formData)
            results = str(results) + " " + units[formDatay["chosen_method"]]
        
    dicc = {"form_choices": form_choices, "form": form, "form_url": form_url,
    "results": results, "explanation": explanation}
    
    return render(request, "calcs/calcs_index.html", dicc)

def ajax_expl(request, method):
    #Choose the correct explanation for each method through ajax request.
    if request.is_ajax():
        explanation = explanations[method]
    return HttpResponse(explanation)
