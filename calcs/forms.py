#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from django import forms
from driade.settings import DATE_INPUT_FORMATS
from django.core.validators import MaxValueValidator, MinValueValidator 

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

class ChillForm(forms.Form):
    
    chosen_method = forms.ChoiceField(choices=chill_choices, label="Método")
    temp = forms.DecimalField(label="Temperatura ºC",
        validators=[MaxValueValidator(60), MinValueValidator(-20)], localize=True)
    base_temp = forms.DecimalField(label="Temperatura base ºC", required=False, 
        validators=[MaxValueValidator(60), MinValueValidator(-20)], localize=True)
    sup_temp = forms.DecimalField(label="Temperatura superior ºC", required=False,
        validators=[MaxValueValidator(60), MinValueValidator(-20)], localize=True)
    
class HeatForm(forms.Form):
    
    chosen_method = forms.ChoiceField(choices=heat_choices, label="Método")
    temp = forms.DecimalField(label="Temperatura ºC",
        validators=[MaxValueValidator(60), MinValueValidator(-20)], localize=True)
    base_temp = forms.DecimalField(label="Temperatura base ºC", required=False, 
        validators=[MaxValueValidator(60), MinValueValidator(-20)], localize=True)
    sup_temp = forms.DecimalField(label="Temperatura superior ºC", required=False,
        validators=[MaxValueValidator(60), MinValueValidator(-20)], localize=True)
    
class EvapoForm(forms.Form):
    
    max_temp = forms.DecimalField(label="Temperatura máxima ºC",
        validators=[MaxValueValidator(60), MinValueValidator(-20)])
    min_temp = forms.DecimalField(label="Temperatura mínima ºC",
        validators=[MaxValueValidator(60), MinValueValidator(-20)])
    humidity = forms.DecimalField(label="Humedad relativa %",
        validators=[MaxValueValidator(100), MinValueValidator(0)])
    wind_speed = forms.DecimalField(label="Velocidad del viento m/s",
        validators=[MaxValueValidator(30), MinValueValidator(0)])
    air_pressure = forms.DecimalField(label="Presión atmosférica mb",
        validators=[MaxValueValidator(1030), MinValueValidator(0)])
    solar_radiation = forms.DecimalField(label="Radiación solar MJ m-2 día-1")
        validators=[MaxValueValidator(50), MinValueValidator(0)]
    latitude = forms.DecimalField(label="Latitud º",
        validators=[MaxValueValidator(90), MinValueValidator(-90)])
    altitude = forms.DecimalField(label="Altura sobre el nivel del mar m",
        validators=[MaxValueValidator(3000), MinValueValidator(0)])
    day = forms.DateField(label="Fecha",input_formats=DATE_INPUT_FORMATS)
