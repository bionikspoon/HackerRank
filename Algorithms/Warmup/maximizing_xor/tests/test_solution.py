from unittest import TestCase
from nose.tools import *

from solution.solution import *


class TestSolution(TestCase):
    def test_case_1(self):
        with open('case1_in.txt') as sample_input:
            case1_in = sample_input.read()
        with open('case1_out.txt') as sample_output:
            case1_out = sample_output.read()

        assert_equal(str(main(case1_in)), case1_out)


    def test_max_xor_of_1_and_10_is_15(self):
        assert_equal(maximize_xor(1, 10), 15)

    def test_max_xor_of_10_and_10_is_0(self):
        assert_equal(maximize_xor(10, 10), 0)

    def test_max_xor_of_10_and_15_is_7(self):
        assert_equal(maximize_xor(10, 15), 7)


if __name__ == '__main__':
    unittest.main()
