#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from django import forms

chill_choices = (
    ("horas_frio", "Horas Frío"),
    ("richardson", "Unidades de Frío Richardson"),
    ("richardson_sin_neg", "Unidades de Frío Richardson corregidas"),
    ("shaltout", "Unidades de Frío Shaltout y Unrath"),
    )

heat_choices = (
    ("dias_grado", "Días grado"),
    ("growing_degree_hours", "Growing Degree Hours"),
    )

class ChillForm(forms.Form):
    
    chill_method = forms.ChoiceField(choices=chill_choices, label="Método")
    temp = forms.DecimalField(label="Temperatura ºC",localize=True)
    base_temp = forms.DecimalField(label="Temperatura base ºC", required=False,localize=True)
    
class HeatForm(forms.Form):
    
    heat_method = forms.ChoiceField(choices=heat_choices, label="Método")
    temp = forms.DecimalField(label="Temperatura ºC")
    base_temp = forms.DecimalField(label="Temperatura base ºC", required=False,localize=True)
    sup_temp = forms.DecimalField(label="Temperatura superior ºC", required=False,localize=True)
    
class EvapoForm(forms.Form):
    
    temp = forms.DecimalField()
    humidity = forms.DecimalField()
    wind_speed = forms.DecimalField()
