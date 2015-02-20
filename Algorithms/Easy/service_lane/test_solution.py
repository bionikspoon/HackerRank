import cStringIO as StringIO
import unittest
import sys
import random

import nose.tools as test
from unittest2.test.support import captured_stdout

import solution


cases = []
case0_in = """
8 5
2 3 1 2 3 2 3 3
0 3
4 6
6 7
3 5
0 7
"""

case0_out = """
1
2
3
2
1
"""
cases.append((case0_in, case0_out))

case1_in = """
5 5
1 2 2 2 1
2 3
1 4
2 4
2 4
2 3
"""

case1_out = """
2
1
1
1
2
"""
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
        n = lambda: random.randint(2, 100000)
        t = lambda: random.randint(1000, 1000)
        i = lambda _n: random.randint(0, _n - 2)
        j = lambda _i, _n: min(random.randint(_i + 1, _n), _i + 999)
        k = lambda: random.randint(1, 3)
        w = lambda _n: ' '.join([str(k()) for _ in range(_n)])

        case_format = lambda *args: '%i %i' % (args)
        input_format = lambda *args: '%s\n%s\n%s' % (args)

        def test_case():
            _i = i(_n)
            _j = j(_i, _n)
            return case_format(_i, _j)

        _n = n()
        _t = t()
        test_input = '\n'.join([test_case() for _ in xrange(_t)])
        test_input = input_format(case_format(_n, _t), w(_n), test_input)
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
    pass


if __name__ == '__main__':
    unittest.main()