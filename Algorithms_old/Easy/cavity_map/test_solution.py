import StringIO as StringIO
import unittest
import sys
import random

import nose.tools as test
from unittest2.test.support import captured_stdout

import solution


cases = []
case0_in = """
4
1112
1912
1892
1234"""

case0_out = """
1112
1X12
18X2
1234"""
cases.append((case0_in, case0_out))

case1_in = """
5
11235
81321
34558
91442
33377"""

case1_out = """
11235
81321
34558
91442
33377"""
cases.append((case1_in, case1_out))

case2_in = """
5
11111
15131
11211
12191
11111"""

case2_out = """
11111
1X1X1
11X11
1X1X1
11111"""
cases.append((case2_in, case2_out))

case3_in = """
1
1"""

case3_out = """
1"""
cases.append((case3_in, case3_out))

case4_in = """
2
22
22"""

case4_out = """
22
22"""
cases.append((case4_in, case4_out))

case5_in = """
3
999
989
999"""

case5_out = """
999
989
999"""
cases.append((case5_in, case5_out))

case6_in = """
3
969
786
979"""

case6_out = """
969
7X6
979"""
cases.append((case6_in, case6_out))

row = "9" * 100
col = (row + '\n') * 100
case7_in = """
100"""
case7_in += '\n' + col

case7_out = col
cases.append((case7_in, case7_out))

case8_in = """
9
123456789
987654321
123456789
987654321
123456789
987654321
123456789
987654321
123456789"""

case8_out = """
123456789
987654321
123456789
987654321
123456789
987654321
123456789
987654321
123456789"""
cases.append((case8_in, case8_out))

case9_in = """
9
919191919
121212121
913131319
121414121
913151319
121414121
913131319
121212121
919191919"""
case9_out = """
919191919
1X1X1X1X1
91X1X1X19
1X1X1X1X1
91X1X1X19
1X1X1X1X1
91X1X1X19
1X1X1X1X1
919191919"""
cases.append((case9_in, case9_out))

case10_in = """
5
11111
11121
11111
11111
11111"""

case10_out = """
11111
111X1
11111
11111
11112"""
cases.append((case10_in, case10_out))


class TestSolutionModule(object):
    def __init__(self):
        global cases
        self.cases = cases
        solution.input = raw_input

    def main_with_input(self, case_input):
        case_input = StringIO.StringIO(case_input)
        sys.stdin = case_input
        with captured_stdout() as result:
            solution.main()
        sys.stdin = sys.__stdin__
        result = result.getvalue().strip()
        self.print_format(result, 'ACTUAL')
        return result

    def test_cases(self):
        for i, (_in, _out) in enumerate(self.cases):
            yield self.check_case, _in.strip(), _out.strip()

    def check_case(self, case_input, expected):

        actual = self.main_with_input(case_input)
        try:
            test.assert_equal(actual.split("\n"), expected.split("\n"))
            test.assert_equal(actual, expected)
        except AssertionError, e:
            self.print_format(expected, 'EXPECTED')
            raise e

    @test.timed(5)
    def test_performance(self):
        n = 100

        def test_case():
            return ''.join(str(random.randint(0, 9)) for _ in range(n))

        case_input = [test_case() for _ in xrange(n)]
        case_input = "\n".join([str(n)] + case_input)

        test.assert_is_not_none(self.main_with_input(case_input))

    @staticmethod
    def print_format(text, tag='', width=70):
        if tag == 'ACTUAL':
            print '\n'
        print '{:><{}}'.format(tag, width)
        print text
        print '{:<>{}}'.format(tag, width)


class TestSolutionUnit(unittest.TestCase):
    def test_cavity_conditions_true_if_lowest(self):
        (i, j) = (1, 1)
        c_map = [[1, 1, 1], [1, 2, 1], [1, 1, 1]]
        test.assert_equal(solution.cavity_conditions((i, j), c_map), True)

    def test_cavity_conditions_false_if_not_lowest_1(self):
        (i, j) = (1, 1)
        c_map = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        test.assert_equal(solution.cavity_conditions((i, j), c_map), False)

    def test_cavity_conditions_false_if_not_lowest_2(self):
        (i, j) = (1, 1)
        c_map = [[1, 2, 1], [1, 2, 1], [1, 1, 1]]
        test.assert_equal(solution.cavity_conditions((i, j), c_map), False)

    def test_cavity_conditions_ignore_corners(self):
        (i, j) = (1, 1)
        c_map = [[2, 1, 2], [1, 2, 1], [2, 1, 2]]
        test.assert_equal(solution.cavity_conditions((i, j), c_map), True)

    def test_cavity_conditions_1_9(self):
        global case8_in
        (i, j) = (3, 1)
        c_map = [[int(cell) for cell in list(line)] for line in
                 case8_in.strip().split()[1:]]
        test.assert_equal(solution.cavity_conditions((i, j), c_map), False)


if __name__ == '__main__':
    unittest.main()
