from unittest import TestCase

from nose.tools import *


class TestSolution(TestCase):
    # @nottest
    def test_case_1(self):
        with open('case1_in.txt') as sample_input:
            case1_in = sample_input.read()
        with open('case1_out.txt') as sample_output:
            case1_out = sample_output.read()

        assert_equal(str(main(case1_in)), case1_out)

    def test_case_2_multiple_changes_with_one_word(self):
        assert_equal(palindrome_maker("zbcda"), 27)
        assert_equal(str(main("1\nzbcda")), '27')


    def test_given_a_palimndrome_return_0(self):
        assert_equal(palindrome_maker("abcba"), 0)
        assert_greater(palindrome_maker("abcbb"), 0)

    def test_find_changes_to_make_case_1(self):
        assert_equal(palindrome_maker("abc"), 2)

    def test_find_changes_to_make_case_2(self):
        assert_equal(palindrome_maker("abcd"), 4)

    def test_find_changes_to_make_case_3(self):
        assert_equal(palindrome_maker("cba"), 2)


if __name__ == '__main__':
    unittest.main()
