import unittest

import computations

class TestComputations(unittest.TestCase):

    def test_add(self):
        # result = computations.add(8,2)
        self.assertEqual(computations.add(8,2),10)
        self.assertEqual(computations.add(2,6),10)
        self.assertEqual(computations.add(1,8),10)
        self.assertEqual(computations.add(3,7),10)
        self.assertEqual(computations.add(5,5),10)
        self.assertEqual(computations.add(10,0),10)
    
    def test_substract(self):
        res = computations.substract(10,5)
        self.assertEqual(res,5)


#if unit tests pass
if __name__ == '__main__':
    unittest.main()



