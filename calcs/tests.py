from django.test import TestCase

class IndexTestCase(TestCase):
    
    def test_index(self):
        
        '''Test to probe existence of each page
        '''
        url_list = ('/', '/calcs/', '/calcs/chill/', '/calcs/heat/', 
        '/calcs/evapo/')
        
        for page in url_list:
            resp = self.client.get(page)
            self.assertEqual(resp.status_code, 200)
    

class AlgoritsmTestCase(TestCase):
    
    def test_algoritms(self):
        
        from calcs.algoritms import algoritms
        #calcule good values first
        values = [
        (("Chill", "horas_frio", {"temp": 7,}), (1)),
        (("Chill", "horas_frio", {"temp": 4, "base_temp": 7}), (1)),
        (("Chill", "horas_frio", {"temp": 9, "base_temp": 7}), (0)),
        (("Chill", "richardson", {"temp": 9}), (1)),
        (("Chill", "richardson", {"temp": 1}), (0)),
        (("Chill", "richardson", {"temp": 17}), (-0.5)),
        (("Chill", "richardson_sin_neg", {"temp": 1.7}), (0.5)),
        (("Chill", "richardson_sin_neg", {"temp": 17}), (0)),
        (("Chill", "shaltout", {"temp": -4}), (0)),
        (("Chill", "shaltout", {"temp": 8}), (1)),
        (("Chill", "shaltout", {"temp": 21}), (-1)),
        (("Heat", "dias_grado", {"temp": 21}), (11)),
        (("Heat", "dias_grado", {"temp": 21, "base_temp": 7}), (14)),
        (("Heat", "dias_grado", {"temp": 21, "base_temp": 7, "sup_temp": 20}), (0)),
        (("Heat", "growing_degree_hours", {"temp": 21}), (19.175507130317943 )),
        (("Heat", "growing_degree_hours", {"temp": 26}), (0.058720259195217284)),
        (("Heat", "growing_degree_hours", {"temp": 37}), (0)),
        (("Evapo", "penman-monteith-fao", {"max_temp": 21.5, "min_temp": 12.3,
        "humidity": 73.5, "wind_speed": 2.078, "air_pressure": 100.1,
        "solar_radiation": 22.07, "latitude": 50.8, "altitude": 100,
        "day": "06/07/2011"}), (3.7424693078655804)),
        ]
        for argument, result in values:
            good_result = algoritms(argument[0], argument[1], argument[2])
            self.assertEquals(good_result, result)
        
