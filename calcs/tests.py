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
    
    def test_forms(self):
        
        from calcs.forms import ChillForm, HeatForm
        
        '''Test to probe chill, heat and evapo forms
        '''
        #first test chill form
        url = "/calcs/chill/"
        chill_good_data = {"chill_method": "horas_frio", "temp": 6}
        form = ChillForm(chill_good_data)
        self.assertTrue(form.is_valid())
