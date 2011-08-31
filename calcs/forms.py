#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from django import forms

class ChillForm(forms.Form):
    
    chill_choices = (
        ("horas_frio", "Horas Frío"),
        ("richardson", "Unidades de Frío Richardson"),
        ("richardson_sin_neg", "Unidades de Frío Richardson corregidas"),
        ("shaltout", "Unidades de Frio Shaltout y Unrath"),
        )
    
    chill_method = forms.ChoiceField(choices=chill_choices, label="Método")
    since = forms.DateField(label="Desde")
    until = forms.DateField(label="Hasta")
    
class HeatForm(forms.Form):
    
    heat_choices = (
        ("dias_grado", "Días grado"),
        ("growing_degree_hours", "Growing Degree Hours"),
        )
    
    heat_method = forms.ChoiceField(choices=heat_choices, label="Método")
    since = forms.DateField(label="Desde")
    until = forms.DateField(label="Hasta")
    
class EvapoForm(forms.Form):
    
    since = forms.DateField(label="Desde")
    until = forms.DateField(label="Hasta")
