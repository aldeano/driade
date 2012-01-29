from django.test import TestCase
from django.core.urlresolvers import reverse
from calcs.algoritms import explanations

class IndexTestCase(TestCase):

    url_list = ('/', '/calcs/chill/', '/calcs/heat/', 
        '/calcs/evapo/')
    
    bad_urls = ('/dsbkjdfb/', '/calcs/casdkfjh/')
    
    ajax_urls = ('horas_frio')
    
    def test_index(self):
        '''Test to probe existence of each page
        '''

        for page in self.url_list:
            resp = self.client.get(page)
            self.assertEqual(resp.status_code, 200)
        
    def test_bad_urls(self):
        ''' it does what it said, test erroneous urls waiting for a 
        404 message'''
        
        for page in self.bad_urls:
            resp = self.client.get(page)
            self.assertEqual(resp.status_code, 404)
    
    def test_post(self):
        '''test post views and forms
        '''
        checkins = (('/calcs/chill/', {'chosen_method': 'horas_frio',
        'temp': 5}, '1 hf'),
        ('/calcs/chill/', {'chosen_method': 'horas_frio', 'temp': 5,
        'base_temp': 4}, '0 hf'),
        ('/calcs/chill/', {'chosen_method': 'richardson', 'temp': 5}, '1 uf'),
        ('/calcs/chill/', {'chosen_method': 'richardson_sin_neg', 'temp': 2}, '0.5 uf'),
        ('/calcs/chill/', {'chosen_method': 'shaltout', 'temp': 21}, '-1 uf'),
        ('/calcs/chill/', {'chosen_method': 'bajas_necesidades', 'temp': 5}, '0.5 uf'),
        ('/calcs/heat/', {'chosen_method': 'dias_grado', 'temp': 21}, '11 dg'),
        ('/calcs/heat/', {'chosen_method': 'dias_grado', 'temp': 14, 
        'base_temp': 15}, '0 dg'),
        ('/calcs/heat/', {'chosen_method': 'dias_grado', 'temp': 31, 
        'sup_temp': 25}, '0 dg'),
        ('/calcs/heat/', {'chosen_method': 'growing_degree_hours', 'temp': 21},
        '19.18 gdh'),
        ('/calcs/heat/', {'chosen_method': 'growing_degree_hours', 'temp': 26},
        '0.06 gdh'),
        ('/calcs/evapo/', {'chosen_method': 'penman_monteith_fao', 'max_temp': 31, 
        'min_temp': 13.2, 'humidity': 56, 'wind_speed': 1.32, 'air_pressure': 984, 
        'solar_radiation': 19.43, 'latitude': -32, 'altitude': 41, 'day': "04/10/2011"},
        '3.42 mm'),
        )
        
        for check in checkins:
            resp = self.client.post(check[0], check[1])
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('results' and 'explanation' in resp.context)
            self.assertEqual(resp.context['results'], check[2])
    
class AlgoritmsTestCase(TestCase):
    
    def test_algoritms(self):
        
        from calcs.algoritms import algoritms
        from datetime import date
        #calcule good values first
        values = [
        (("chill", {"chosen_method": "horas_frio", "temp": 7, "base_temp": None}), (1)),
        (("chill", {"chosen_method": "horas_frio", "temp": 8, "base_temp": None}), (0)),
        (("chill", {"chosen_method": "horas_frio", "temp": 4, "base_temp": 7}), (1)),
        (("chill", {"chosen_method": "horas_frio", "temp": 9, "base_temp": 7}), (0)),
        (("chill", {"chosen_method": "richardson", "temp": 9}), (1)),
        (("chill", {"chosen_method": "richardson", "temp": 1}), (0)),
        (("chill", {"chosen_method": "richardson", "temp": 17}), (-0.5)),
        (("chill", {"chosen_method": "richardson_sin_neg", "temp": 1.7}), (0.5)),
        (("chill", {"chosen_method": "richardson_sin_neg", "temp": 17}), (0)),
        (("chill", {"chosen_method": "shaltout", "temp": -4}), (0)),
        (("chill", {"chosen_method": "shaltout", "temp": 8}), (1)),
        (("chill", {"chosen_method": "shaltout", "temp": 21}), (-1)),
        (("chill", {"chosen_method": "bajas_necesidades", "temp": 1}), (0)),
        (("chill", {"chosen_method": "bajas_necesidades", "temp": 9}), (1)),
        (("chill", {"chosen_method": "bajas_necesidades", "temp": 22}), (-1)),
        (("heat", {"chosen_method": "dias_grado", "temp": 21, "base_temp": None, "sup_temp": None}), (11)),
        (("heat", {"chosen_method": "dias_grado", "temp": 21, "base_temp": 7, "sup_temp": None}), (14)),
        (("heat", {"chosen_method": "dias_grado", "temp": 21, "base_temp": None, "sup_temp": 20}), (0)),
        (("heat", {"chosen_method": "growing_degree_hours", "temp": 21}), (19.18 )),
        (("heat", {"chosen_method": "growing_degree_hours", "temp": 26}), (0.06)),
        (("heat", {"chosen_method": "growing_degree_hours", "temp": 37}), (0)),
        (("evapo", {"chosen_method": "penman_monteith_fao", "max_temp": 21.5, 
        "min_temp": 12.3, "humidity": 73.5, "wind_speed": 2.078, 
        "air_pressure": 100.1, "solar_radiation": 22.07, "latitude": 50.8,
        "altitude": 100, "day": date(2011, 7, 6)}), (3.74)),
        ]
        for argument, result in values:
            good_result = algoritms(argument[0], argument[1])
            self.assertEquals(good_result, result)
