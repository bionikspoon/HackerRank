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
4
6
1 4 5 7 9 12
"""

case0_out = """
1
"""
cases.append((case0_in, case0_out))


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
        v = random.randint(-1000, 1000)
        n = random.randint(1000,1000)
        an = [str(random.randint(1, 1000)) for _ in xrange(n)]
        an.append(str(v))
        test_input = "{:d}\n{:d}\n{}".format(v, n, ' '.join(an))

        print test_input
        test.assert_is_not_none(self.main_with_input(test_input))

    @staticmethod
    def print_format(text, tag='', width=70):
        if tag == 'ACTUAL':
            print '\n'
        print '{:><{}}'.format(tag, width)
        pprint(text)
        print '{:<>{}}'.format(tag, width)


class TestSolutionUnit(unittest.TestCase):
    def test_something(self):
        test.assert_equal(False, False)


if __name__ == '__main__':
    unittest.main()