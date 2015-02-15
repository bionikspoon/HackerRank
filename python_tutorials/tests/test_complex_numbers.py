import unittest
from python_tutorials.class_1_dealing_with_complex_numbers import ComplexNumber, \
    main


class TestComplexNumbers(unittest.TestCase):
    def setUp(self):
        self.c = ComplexNumber(2, 1)
        self.d = ComplexNumber(5, 6)

    def test_prints_correct_format(self):
        test_number = ComplexNumber(1, 1)
        self.assertEqual(str(test_number), "1.00 + 1.00i")

    def test_prints_only_a_when_b_is_zero(self):
        test_number = ComplexNumber(1, 0)
        self.assertEqual(str(test_number), "1.00")

    def test_uses_minus_sign_for_negative_b(self):
        test_number = ComplexNumber(1, -1)
        self.assertEqual(str(test_number), "1.00 - 1.00i")

    def test_uses_minus_sign_for_negative_a(self):
        test_number = ComplexNumber(-1, -1)
        self.assertEqual(str(test_number), "-1.00 - 1.00i")
        test_number = ComplexNumber(-1, 1)
        self.assertEqual(str(test_number), "-1.00 + 1.00i")

    def test_prints_zero_if_and_b_are_zero(self):
        test_number = ComplexNumber(0, 0)
        self.assertEqual(str(test_number), "0.00")

    def test_only_b_if_no_a(self):
        test_number = ComplexNumber(0, 1)
        self.assertEqual(str(test_number), "1.00i")
        test_number = ComplexNumber(0, -1)
        self.assertEqual(str(test_number), "-1.00i")

    def test_addition(self):
        self.assertEqual(str(self.c + self.d), "7.00 + 7.00i")

    def test_subtraction(self):
        self.assertEqual(str(self.c - self.d), "-3.00 - 5.00i")

    def test_multiplication(self):
        self.assertEqual(str(self.c * self.d), "4.00 + 17.00i")

    def test_division(self):
        self.assertEqual(str(self.c / self.d), "0.26 - 0.11i")

    def test_mod(self):
        self.assertEqual(self.c.mod, "2.24")
        self.assertEqual(self.d.mod, "7.81")

    def test_main(self):
        test_input = ["2 1", "5 6"]
        test_output = """7.00 + 7.00i
-3.00 - 5.00i
4.00 + 17.00i
0.26 - 0.11i
2.24
7.81"""
        self.assertEqual(main(test_input), test_output)

        test_input = ["5.9 6", "9 10"]
        test_output = """14.90 + 16.00i
-3.10 - 4.00i
-6.90 + 113.00i
0.62 - 0.03i
8.41
13.45"""
        self.assertEqual(main(test_input), test_output)


if __name__ == '__main__':
    unittest.main()
