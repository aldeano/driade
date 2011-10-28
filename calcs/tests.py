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
        (("Chill", "horas_frio", {"temp": 4, "base_temp": 7}), (1)),
        (("Chill", "horas_frio", {"temp": 9, "base_temp": 7}), (0)),
        (("Chill", "richardson", {"temp": 9}), (1)),
        ]
        for attempt, result in values:
            good_result = algoritms(attempt[0], attempt[1], attempt[2])
            self.assertEquals(good_result, result)
        
