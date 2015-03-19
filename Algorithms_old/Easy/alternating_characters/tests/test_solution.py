from unittest import TestCase

from nose.tools import *


class TestSolution(TestCase):
    @nottest
    def test_case_1(self):
        with open('case1_in.txt') as sample_input:
            case1_in = sample_input.read()
        with open('case1_out.txt') as sample_output:
            case1_out = sample_output.read()

        assert_equal(str(main(case1_in)), case1_out)

    def test_alternating_case_1(self):
        assert_equal(alternating_characters("AAAA"), 3)

    def test_alternating_case_2(self):
        assert_equal(alternating_characters("BBBBB"), 4)

    def test_alternating_case_3(self):
        assert_equal(alternating_characters("ABABABAB"), 0)

    def test_alternating_case_4(self):
        assert_equal(alternating_characters("BABABA"), 0)

    def test_alternating_case_5(self):
        assert_equal(alternating_characters("AAABBB"), 4)

if __name__ == '__main__':
    unittest.main()
