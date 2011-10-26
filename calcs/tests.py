from django.test import TestCase

class IndexTestCase(TestCase):
    
    def test_index(self):
        
        '''Test to probe existence of each page
        '''
        resp_index = self.client.get('/')
        resp_index_calcs = self.client.get('/calcs/')
        resp_index_chill = self.client.get('/calcs/chill/')
        resp_index_heat = self.client.get('/calcs/heat/')
        resp_index_evapo = self.client.get('/calcs/evapo/')
        self.assertEqual(resp_index.status_code, 200)
        self.assertEqual(resp_index_calcs.status_code, 200)
        self.assertEqual(resp_index_chill.status_code, 200)
        self.assertEqual(resp_index_heat.status_code, 200)
        self.assertEqual(resp_index_evapo.status_code, 200)
    

class AlgoritsmTestCase(TestCase):
    
    def test_algoritms(self):
        
        from calcs.algoritms import algoritms
        #calcule good values first
        values = [
        (("Chill", "horas_frio", {"temp": 4, "base_temp": 7}), (1)),
        (("Chill", "horas_frio", {"temp": 9, "base_temp": 7}), (0)),
        ]
        for attempt, result in values:
            good_result = algoritms(attempt[0], attempt[1], attempt[2])
            self.assertEquals(good_result, result)
        
