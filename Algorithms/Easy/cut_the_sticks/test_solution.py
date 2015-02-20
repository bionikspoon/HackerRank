import cStringIO as StringIO
import unittest
import sys
import random

import nose.tools as test
from unittest2.test.support import captured_stdout

import solution


cases = []
case0_in = """
6
5 4 4 2 2 8"""

case0_out = """
6
4
2
1"""
cases.append((case0_in, case0_out))

case1_in = """
8
1 2 3 4 3 3 2 1"""

case1_out = """
8
6
4
1"""
cases.append((case1_in, case1_out))


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
        t = 1
        n = (1, 1000)
        a1 = (1, 1000)
        case_format = lambda _n, _a1: '%i\n%s' % (_n, _a1)
        input_format = lambda case: '\n'.join(case)

        def test_case():
            _n = random.randint(n[0], n[1])
            _n = n[1]
            _a1 = ' '.join(
                [str(random.randint(a1[0], a1[1])) for _ in xrange(_n)])
            return case_format(_n, _a1)

        test_input = [test_case() for _ in xrange(t)]
        test_input = input_format(test_input)
        print test_input
        self.main_with_input(test_input)

    @staticmethod
    def print_format(text, tag='', width=70):
        if tag == 'ACTUAL':
            print '\n'
        print '{:><{}}'.format(tag, width)
        print text
        print '{:<>{}}'.format(tag, width)


class TestSolutionUnit(unittest.TestCase):
    def test_something(self):
        test.assert_equal(True, True)


if __name__ == '__main__':
    unittest.main()