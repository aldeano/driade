#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from django import forms
from django.shortcuts import render
from calcs.forms import ChillForm, HeatForm, EvapoForm, heat_choices, chill_choices
from calcs.algoritms import *

def home(request):
    return render(request, "calcs/calcs_index.html")
    
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
            
def chill(request):
    form = ChillForm()
    results = None
    
    if request.method == "POST":
        form = ChillForm(request.POST)
        if form.is_valid():
            method = form.cleaned_data["chosen_method"]
            temp_calc = form.cleaned_data["temp"]
            temp_base = form.cleaned_data["base_temp"]
            #comprobar si se usa temperatura base personalizada o
            #por defecto (=7,2ºC)
            if temp_base == None:
                temp_base = 7.22
            #averigua qué método seleccionó el usuario y procede a obtener
            #el resultado.
            if method == "horas_frio":                
                if 0 < temp_calc < temp_base:
                    chill_index = 1
                else:
                    chill_index =0
            elif method == "richardson":
                if temp_calc <= 1.4:
                    chill_index = 0
                elif 1.4 < temp_calc <= 2.4:
                    chill_index = 0.5
                elif 2.4 < temp_calc <= 9.1:
                    chill_index = 1
                elif 9.1 < temp_calc <= 12.4:
                    chill_index = 0.5
                elif 12.4 < temp_calc <=  15.9:
                    chill_index = 0
                elif 15.9 < temp_calc <= 18:
                    chill_index = -0.5
                else:
                    chill_index = -1
            elif method == "richardson_sin_neg":
                if 1.4 < temp_calc <= 2.4:
                    chill_index = 0.5
                elif 2.4 < temp_calc <= 9.1:
                    chill_index = 1
                elif 9.1 < temp_calc <= 12.4:
                    chill_index = 0.5
                else:
                    chill_index = 0
            elif method == "shaltout":
                if temp_calc <= 1.6:
                    chill_index = 0
                elif 1.6 < temp_calc <= 7.2:
                    chill_index = 0.5
                elif 7.2 < temp_calc <= 13:
                    chill_index = 1
                elif 13 < temp_calc <= 16.5:
                    chill_index = 0.5
                elif 16.5 < temp_calc <= 19:
                    chill_index = 0
                elif 19 < temp_calc <= 20.7:
                    chill_index = -0.5
                elif 20.7 < temp_calc <= 22.1:
                    chill_index = -1
                elif 22.1 < temp_calc <= 23.3:
                    chill_index = -1.5
                else:
                    chill_index = -2
            else:
                raise forms.ValidationError("Elige un método de la lista")
                
            #finalmente pone el resultado disponible para el template
            for sublist in chill_choices:
                if sublist[0] == method:
                    print_method = sublist[1]
                    break
            results = "%s = %s" % (print_method, chill_index)
            
    dicc = {"chill_form": form, "results": results}
    
    return render(request, "calcs/chill.html", dicc)
    
def heat(request):
    form = HeatForm()
    results = None
    
    if request.method == "POST":
        form = HeatForm(request.POST)
        if form.is_valid():
            method = form.cleaned_data["chosen_method"]
            temp_calc = form.cleaned_data["temp"]
            temp_base = form.cleaned_data["base_temp"]
            temp_sup = form.cleaned_data["sup_temp"]
            #comprobar si se usa temperatura base y superior
            #personalizada o por defecto (10ºC a 30ºC)
            if temp_base == None:
                temp_base = 10
            if temp_sup == None:
                temp_sup = 30
            #averigua qué método seleccionó el usuario y procede a obtener
            #el resultado.
            if method == "dias_grado":
                if temp_base < temp_calc < temp_sup:
                    heat_index = temp_calc - temp_base
                else:
                    heat_index = 0
            elif method == "growing_degree_hours":
                if 4 < temp_calc < 25:
                    heat_index = 10.5*(1 + math.cos(math.pi + math.pi*((float(temp_calc) - 4)/21)))
                elif 25 <= temp_calc < 36:
                    heat_index = 21*(1 + math.cos((math.pi/2) + (math.pi/2)*((float(temp_calc) - 4)/21)))
                else:
                    heat_index = 0
            else:
                raise forms.ValidationError("Elige un método de la lista")
            
            #finalmente pone el resultado disponible para el template
            for sublist in heat_choices:
                if sublist[0] == method:
                    print_method = sublist[1]
                    break
            results = "%s = %s" % (print_method, heat_index)
    
    dicc = {"heat_form": form, "results": results}
    
    return render(request, "calcs/heat.html", dicc)
    
def evapo(request):
    form = EvapoForm()
    dicc = {"evapo_form": form}
    return render(request, "calcs/evapo.html", dicc)
    
