import unittest

from solution.solution import main


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        with open('case1_in.txt') as sample_input:
            case_1 = sample_input.read()
        with open('case1_out.txt') as sample_output:
            case_1_out = sample_output.read()

        self.assertEqual(str(main(case_1)), case_1)


if __name__ == '__main__':
    unittest.main()
