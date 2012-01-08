#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from django import forms
from driade.settings import DATE_INPUT_FORMATS

chill_choices = (
    ("horas_frio", "Horas Frío"),
    ("richardson", "Unidades de Frío Richardson"),
    ("richardson_sin_neg", "Unidades de Frío Richardson corregidas"),
    ("shaltout", "Unidades de Frío Shaltout y Unrath"),
    ("bajas_necesidades", "Unidades de frío para bajas necesidades"),
    )

heat_choices = (
    ("dias_grado", "Días grado"),
    ("growing_degree_hours", "Growing Degree Hours"),
    )

class TempField(forms.DecimalField):
    
    def clean(self, value):
        value = super(TempField, self).clean(value)
        if -20 < value < 60:
            raise ValidationError
        else:
            return value
        
class ChillForm(forms.Form):
    
    chosen_method = forms.ChoiceField(choices=chill_choices, label="Método", initial='horas_frio')
    temp = forms.DecimalField(label="Temperatura ºC",localize=True)
    base_temp = forms.DecimalField(label="Temperatura base ºC", required=False,localize=True)
    sup_temp = forms.DecimalField(label="Temperatura superior ºC", required=False,localize=True)
    
class HeatForm(forms.Form):
    
    chosen_method = forms.ChoiceField(choices=heat_choices, label="Método", initial="dias_grado")
    temp = TempField(label="Temperatura ºC")
    base_temp = forms.DecimalField(label="Temperatura base ºC", required=False,localize=True)
    sup_temp = forms.DecimalField(label="Temperatura superior ºC", required=False,localize=True)
    
class EvapoForm(forms.Form):
    
    max_temp = forms.DecimalField(label="Temperatura máxima ºC")
    min_temp = forms.DecimalField(label="Temperatura mínima ºC")
    humidity = forms.DecimalField(label="Humedad relativa %")
    wind_speed = forms.DecimalField(label="Velocidad del viento m/s")
    air_pressure = forms.DecimalField(label="Presión atmosférica mb")
    solar_radiation = forms.DecimalField(label="Radiación solar MJ m-2 día-1")
    latitude = forms.DecimalField(label="Latitud º")
    altitude = forms.DecimalField(label="Altura sobre el nivel del mar m")
    day = forms.DateField(label="Fecha",input_formats=DATE_INPUT_FORMATS)
