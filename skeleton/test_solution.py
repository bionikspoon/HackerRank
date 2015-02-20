import StringIO
import unittest
import sys
import random

import nose.tools as test
from unittest2.test.support import captured_stdout

import solution


cases = []
case0_in = """
2
2 3
3 7"""

case0_out = """
5
10"""
cases.append((case0_in, case0_out))
case1_in = """
3
1 1
2 2
3 3"""

case1_out = """
2
4
6"""
cases.append((case1_in, case1_out))


class TestSolution(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        global cases
        self.cases = cases
        solution.input = raw_input
        super(TestSolution, self).__init__(*args, **kwargs)

    def main_with_input(self, case_input):
        case_input = StringIO.StringIO(case_input)
        sys.stdin = case_input
        result = solution.main()
        sys.stdin = sys.__stdin__
        return result

    def test_cases(self):
        for i, (_in, _out) in enumerate(self.cases):
            self.check_case(_in.strip(), _out.strip())

    def check_case(self, case_input, expected):
        with captured_stdout() as actual:
            self.main_with_input(case_input)
        actual = actual.getvalue().strip()

        test.assert_equal(actual.split("\n"), expected.split("\n"))
        test.assert_equal(actual, expected)

    @test.timed(5)
    def test_performance(self):
        t = 1000

        def test_case():
            a = random.randint(1, 1000)
            b = random.randint(1, 1000)
            return "%i %i" % (a, b)

        case_data = [test_case() for _ in xrange(t)]
        case_data = "\n".join([str(t)] + case_data)

        self.main_with_input(case_data)


if __name__ == '__main__':
    unittest.main()
