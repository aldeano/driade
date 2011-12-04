#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import math
from datetime import datetime, timedelta

explanations = {"horas_frio": "Horas entre ciertas temperaturas, si no se " \
    "detalla se ocupa 7,22º y 0º C como estandar", 
    "richardson": "Cuantificación del frío acumulado según los trabajos " \
    "de Richardson (1974) en los cuales se asigna mayor efecto a temperaturas " \
    "cercanas a 5º C", 
    "richardson_sin_neg": "Cuantificación del frío acumulado según los trabajos " \
    "de Richardson (1974) en los cuales se asigna mayor efecto a temperaturas " \
    "cercanas a 5º C. Sin efectos negativos, adecuado para zonas con inviernos", \
    "suaves.", 
    "shaltout": "Cuantificación del frío acumulado según los trabajos " \
    "de Shaltout (1983) en los cuales se asigna mayor efecto a temperaturas " \
    "cercanas a 7,2º C",
    "dias_grado": "Grados ºC entre ciertas temperaturas, si no se detalla " \
    "se ocupa 10º y 30º C como estandar",
    "growing-degree_hours": "Estimación del efecto de la tempratura sobre " \
    "el desarrollo fenológico basado en una curva cuyo óptimo está en los " \
    "25º C. Basado en el trabajo de Anderson & Richardson (1986)", 
    "evapotranspiración": "Milímetros de agua evaporada por una superficie " \
    "estandar de pasto en condiciones ideales. Se usa el método propuesto " \
    "por FAO, publicación nº 56",}

units = {"horas_frio": "hf", "richardson": "uf", "richardson_sin_neg": "uf",
    "shaltout": "uf", "dias_grado": "dg", "growing_degree_hours": "gdh"}

def algoritms(phenologic_calc, kwdata):
    '''calc's algoritms, it needs data inside a dictionary'''
      
    if phenologic_calc == "Chill":
        
        temp_calc = kwdata["temp"]
        
        if kwdata["chosen_method"] == "horas_frio":
            if kwdata["base_temp"] != None:
                temp_base = kwdata["base_temp"]                
            else:
                temp_base = 7.22
            if 0 < temp_calc < temp_base:
                result = 1
            else:
                result = 0
        elif kwdata["chosen_method"] == "richardson":
            if temp_calc <= 1.4:
                result = 0
            elif 1.4 < temp_calc <= 2.4:
                result = 0.5
            elif 2.4 < temp_calc <= 9.1:
                result = 1
            elif 9.1 < temp_calc <= 12.4:
                result = 0.5
            elif 12.4 < temp_calc <=  15.9:
                result = 0
            elif 15.9 < temp_calc <= 18:
                result = -0.5
            else:
                result = -1
        elif kwdata["chosen_method"] == "richardson_sin_neg":
            if 1.4 < temp_calc <= 2.4:
                result = 0.5
            elif 2.4 < temp_calc <= 9.1:
                result = 1
            elif 9.1 < temp_calc <= 12.4:
                result = 0.5
            else:
                result = 0
        elif kwdata["chosen_method"] == "shaltout":
            if temp_calc <= 1.6:
                result = 0
            elif 1.6 < temp_calc <= 7.2:
                result = 0.5
            elif 7.2 < temp_calc <= 13:
                result = 1
            elif 13 < temp_calc <= 16.5:
                result = 0.5
            elif 16.5 < temp_calc <= 19:
                result = 0
            elif 19 < temp_calc <= 20.7:
                result = -0.5
            elif 20.7 < temp_calc <= 22.1:
                result = -1
            elif 22.1 < temp_calc <= 23.3:
                result = -1.5
            else:
                result = -2
        else:
            raise forms.ValidationError("Elige un método de la lista")
                
    elif phenologic_calc == "Heat":
        
        temp_calc = kwdata["temp"]
        
        if kwdata["chosen_method"] == "dias_grado":
            #if the user don't put personalized values, use standard ones
            #base temp 10ºC and superior temp 30ºC
            if kwdata["base_temp"] != None:
                temp_base = kwdata["base_temp"]                
            else:
                temp_base = 10
            if kwdata["sup_temp"] != None:
                temp_sup = kwdata["sup_temp"]                
            else:
                temp_sup = 30
            #make calcs
            if temp_base < temp_calc < temp_sup:
                result = temp_calc - temp_base
            else:
                result = 0
        elif kwdata["chosen_method"] == "growing_degree_hours":
            if 4 < temp_calc < 25:
                result = 10.5*(1 + math.cos(math.pi + math.pi*((float(temp_calc) - 4)/21)))
            elif 25 <= temp_calc < 36:
                result = 21*(1 + math.cos((math.pi/2) + (math.pi/2)*((float(temp_calc) - 4)/21)))
            else:
                result = 0
        else:
            raise forms.ValidationError("Elige un método de la lista")
            
    elif phenologic_calc == "Evapo":
        
        if kwdata["chosen_method"] == "penman-monteith-fao":        
            #First obtain diary net radiation
            day = kwdata["day"]
            date_calc = datetime.strptime(day, "%d/%m/%Y")
            #To get the julian date compare the first day of the year and the given date
            #Get the seconds of that difference and divide by all the seconds in a day - 86400 - and plus one
            julian_date = (date_calc - datetime(date_calc.year, 1, 1)).total_seconds()/86400 + 1
            relative_distance = 1 + 0.033 * math.cos((2 * math.pi / 365)*julian_date)
            solar_decline = 0.409 * math.sin((2 * math.pi / 365) * julian_date - 1.39)
            lat_grad = kwdata["latitude"]
            lat_rad = math.pi/180 * lat_grad
            sun_angle = math.acos(-math.tan(lat_rad)*math.tan(solar_decline))
            #first radiation index, extraterrestrial radiation
            extrat_rad = ((24*60)/math.pi)*0.082*relative_distance*(sun_angle*math.sin(lat_rad)*math.sin(solar_decline)+math.cos(lat_rad)*math.cos(solar_decline)*math.sin(sun_angle))
            altitude = kwdata ["altitude"]
            #second one, clear day radiation
            clear_day_rad = (0.75 + 2e-5 * altitude)*extrat_rad
            max_temp = kwdata["max_temp"] + 273.15
            min_temp = kwdata["min_temp"] + 273.15
            mid_temp = (max_temp + min_temp)/2 - 273.15
            solar_rad = kwdata["solar_radiation"]
            humidity = kwdata["humidity"]
            sat_vapor_pressure = 0.6108*math.exp((17.27*mid_temp)/(mid_temp + 237.3))
            vapor_pressure = (humidity*sat_vapor_pressure)/100
            #now mix extraterrestrial, clear day & solar radiation to get net long radiation
            net_long_rad = 4.903e-9*((max_temp**4 + min_temp**4)/2)*(0.34-0.14*math.sqrt(vapor_pressure))*(1.35*(solar_rad/clear_day_rad)-0.35)
            #net short radiation, easy one
            net_short_rad = (1-0.23)*solar_rad
            net_radiation = net_short_rad - net_long_rad
            #we got it!!!
            #now got the evapotranspiration
            air_pressure = kwdata["air_pressure"]
            wind_speed = kwdata["wind_speed"]
            latent_heat = 2.501 - mid_temp * (2.361e-3)
            psicometric_constant = 0.00163*(air_pressure/latent_heat)
            curve_slope = (4098*sat_vapor_pressure)/((mid_temp + 237.3)**2)
            pressure_deficit = sat_vapor_pressure - vapor_pressure
            
            result = (0.408*curve_slope*net_radiation+psicometric_constant*(900/(mid_temp+273))*wind_speed*pressure_deficit)/(curve_slope+psicometric_constant*(1+0.34*wind_speed))
            
        else:
            raise forms.ValidationError("Elige un método de la lista")
            
    else:
        raise forms.ValidationError("Elige un método de la lista")
    
    return result
