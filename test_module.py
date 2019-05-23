import module
import unittest

class Test(unittest.TestCase):

    def test_function(self):
        f=module.Series(0,[])
        return True
        
    def test_get_value(self):
        s=module.Series(3,[1,1/2,1/6])
        y=s.get_value(1.0)
        self.assertAlmostEqual(y,1.67,places=2)

    def test_get_derivative(self):
        s=module.Series(3,[1,1/2,1/6])
        y=s.get_derivative(1.0)
        self.assertAlmostEqual(y,0.83,places=2)
        
def error_test():
    s=module.Series(3,[1,1/2,1/6])
    s.get_error(1)
    return True
