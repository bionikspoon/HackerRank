from unittest import TestCase

from nose.tools import *


class TestSolution(TestCase):
    def test_case_1(self):
        with open('case1_in.txt') as sample_input:
            case1_in = sample_input.read()
        with open('case1_out.txt') as sample_output:
            case1_out = sample_output.read()

        self.assertEqual(main(case1_in), case1_out)
        self.assertEqual(str(main(case1_in)), case1_out)

    def test_other_cases(self):
        assert_equal(utopian_tree(4), 7)
        assert_equal(utopian_tree(3), 6)

    def test_height_is_one_if_zero_cycles(self):
        assert_equal(utopian_tree(0), 1)

    def test_height_is_two_after_one_cycle(self):
        assert_equal(utopian_tree(1), 2)


if __name__ == '__main__':
    unittest.main()
