from nose.tools import *
from solution import *

cases = []
case0_in = """
2
3 9
17 24"""

case0_out = """
2
0"""
cases.append((case0_in, case0_out))

case1_in = """
1
4 9
5 8
1 10"""

case1_out = """
2
0
3"""
cases.append((case1_in, case1_out))



def test_cases():
    global cases
    for i, (_in, _out) in enumerate(cases):
        yield check_case, _in.strip(), _out.strip()


# noinspection PyUnusedLocal
def check_case(_in, _out):
    actual = main(_in.split("\n"))
    actual = actual if isinstance(actual, list) else [actual]
    expected = _out.split("\n")
    assert_equals(actual, expected)