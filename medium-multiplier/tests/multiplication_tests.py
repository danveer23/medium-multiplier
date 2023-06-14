import unittest
from medium_multiply import Multiplication


class MultiplicationTestCase(unittest.TestCase):
    def setUp(self):
        self.multiplications = Multiplication(2)

    def test_zero(self):
        """Test 0 multiplied by 2"""

        # 0 multiplied by 2 return 0
        result = self.multiplications.multiply(0)
        self.assertEqual(result, 0)

    def test_natural_number(self):
        """Test natural number 5 multiplied by 2"""

        # 5 multiplied by 2 return 10
        result = self.multiplications.multiply(5)
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()
