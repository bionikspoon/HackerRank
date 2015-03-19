import cStringIO as StringIO
import unittest
import sys
import random

import nose.tools as test
from unittest2.test.support import captured_stdout

import solution


cases = []
case0_in = """
2
3
1 2 3
4
1 2 3 3
"""

case0_out = """
NO
YES
"""
cases.append((case0_in, case0_out))

case1_in = """
4
1
1
2
2 2
2
9 10
3
1 2 2
"""

case1_out = """
YES
NO
NO
NO
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
        t = (10, 10)
        n = (10 ** 5, 10 ** 5)
        a1 = (1, 2 * 10 ** 4)
        case_format = lambda _n, _a1: '%i\n%s' % (_n, _a1)
        input_format = lambda _t, _cases: '%i\n%s' % (_t, '\n'.join(_cases))

        def test_case():
            _n = random.randint(n[0], n[1])
            _a1 = ' '.join(
                [str(random.randint(a1[0], a1[1])) for _ in xrange(_n)])
            return case_format(_n, _a1)

        t = random.randint(t[0], t[1])
        test_input = [test_case() for _ in xrange(t)]
        test_input = input_format(t, test_input)
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
    def test_2_and_2_is_false(self):
        test.assert_equal(solution.has_sum_median([2, 2]), False)


if __name__ == '__main__':
    unittest.main()