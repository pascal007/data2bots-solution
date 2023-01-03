import unittest, os, json

class TestSchemaGenerator(unittest.TestCase):
    
    def test_correct_data(self):
        """This checks to make sure data is correct json"""
        read_path = os.getcwd() + '/data/'
        files = os.listdir(read_path)
        for file in files:
            self.assertTrue(file.endswith('.json'))
            f = open(read_path + file)    
            data = json.load(f)
            self.assertTrue(data.get('message'))
            f.close()
        
        
        
        
        
        