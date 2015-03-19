import unittest

from solution import main


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        with open('case1_in.txt') as sample_input:
            case_1 = sample_input.read()
        case_1_output = "5"
        self.assertEqual(str(main(case_1)), case_1_output)


if __name__ == '__main__':
    unittest.main()
