import unittest
from logger import Logger

class LoggerTest(unittest.TestCase):
    
    def test_info(self):
        '''Tests the info function'''
        log = Logger()
        log.info("Info test")
        self.assertEqual(t.get_text(), "[INFO] Info test")
    
    def test_error(self):
        '''Test the error function'''
        log = Logger()
        log.error("Error test")
        self.assertEqual(t.get_text(), "[WARNING] Error test")

class Target():
    t = Target()
    t.set_text()
    t.get_text()