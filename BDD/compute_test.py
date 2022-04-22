import unittest
from mathcompute import MathCompute

class TestMathCompute(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_compute = MathCompute()

    def test_add(self):
        result = self.new_compute.add(10,5)
        self.assertTrue(result,15)


if __name__ == '__main__':
    unittest.main()
