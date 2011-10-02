#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from django.shortcuts import render
from calcs.forms import ChillForm, HeatForm, EvapoForm, heat_choices, chill_choices

def home(request):
    return render(request, "calcs/calcs_index.html")
    
def chill(request):
    form = ChillForm()
    results = None
    
    if request.method == "POST":
        form = ChillForm(request.POST)
        if form.is_valid():
            method = form.cleaned_data["chill_method"]
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
    dicc = {"heat_form": form}
    return render(request, "calcs/heat.html", dicc)
    
def evapo(request):
    form = EvapoForm()
    dicc = {"evapo_form": form}
    return render(request, "calcs/evapo.html", dicc)
    
