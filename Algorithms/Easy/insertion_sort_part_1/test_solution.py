import cStringIO as StringIO
from pprint import pprint
import string
import unittest
import sys
import random

import nose.tools as test
from unittest2.test.support import captured_stdout

import solution


cases = []
case0_in = """
5
2 4 6 8 3
"""

case0_out = """
2 4 6 8 8
2 4 6 6 8
2 4 4 6 8
2 3 4 6 8
"""
cases.append((case0_in, case0_out))

case1_in = """
1
2
"""

case1_out = """
2
"""
cases.append((case1_in, case1_out))

case2_in = """
5
-2 -1 0 1 -1
"""

case2_out = """
-2 -1 0 1 1
-2 -1 0 0 1
-2 -1 -1 0 1
"""
cases.append((case2_in, case2_out))

case3_in = """
2
0 -1
"""

case3_out = """
0 0
-1 0
"""
cases.append((case3_in, case3_out))

case4_in = """
2
0 1
"""

case4_out = """
0 1
"""
cases.append((case4_in, case4_out))


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

    def check_case(self, case_input, expected):

        actual = self.main_with_input(case_input)
        try:
            test.assert_equal(actual.split("\n"), expected.split("\n"))
            test.assert_equal(actual, expected)
        except:
            self.print_format(expected, 'EXPECTED')
            raise

    def test_cases(self):
        for (_in, _out) in self.cases:
            yield self.check_case, _in.strip(), _out.strip()

    @test.timed(5)
    def test_performance(self):
        n = random.randint(1**3, 1**3)
        an = [str(random.randint(-1*1**4, 1**4)) for _ in xrange(n)]
        test_input = "{:d}\n{}".format(n, ' '.join(an))

        print test_input
        test.assert_is_not_none(self.main_with_input(test_input))

    @staticmethod
    def print_format(text, tag='', width=70):
        if tag == 'ACTUAL':
            print '\n'
        print '{:><{}}'.format(tag, width)
        print(text)
        print '{:<>{}}'.format(tag, width)


class TestSolutionUnit(unittest.TestCase):
    def test_something(self):
        test.assert_equal(False, False)


if __name__ == '__main__':
    unittest.main()