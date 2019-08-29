import unittest     # Import the Python unit testing framework
import maths        # Our code to test


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add(self):
        ''' Tests the add function. '''
        result = maths.add(5,5,16)
        self.assertEqual(result, 'A', "The add function returned an incorrect value!")

    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''
        result = maths.fibonacci(5)
        self.assertEqual(result, '5', "Fibonacci incorecct")
    
    def test_convert_base_under_ten(self):
        '''tests to conver_base function with a base under 10'''
        result = maths.convert_base(45, 7)
        self.assertEqual(result, '3', "Under 10 Fuction failed")
    
    def test_convert_base_over_10(self):
        '''Tests to convert_base function with a base over 10'''
        result = maths.convert_base(45, 16)
        self.assertEqual(result, 'D', "Over 10 Funtion failed")
    
    
        

# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
