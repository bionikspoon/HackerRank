import unittest
from python_tutorials.class_2_find_the_torsional_angle import main


class MyTestCase(unittest.TestCase):
    case1_in = """0 4 5
1 7 6
0 5 9
1 7 2"""
    case1_out = """8.19"""

    case2_in = """5 8.8 9
4 -1 3
7 8.7 3.3
4.4 5.1 6.3"""
    case2_out = """5.69"""

    def test_case_1(self):
        self.assertEqual(main(self.case1_in), self.case1_out)

    def test_case_2(self):
        self.assertEqual(main(self.case2_in), self.case2_out)


if __name__ == '__main__':
    unittest.main()
