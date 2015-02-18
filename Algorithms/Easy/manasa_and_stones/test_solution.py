from nose.tools import *
from solution import *

cases = []
case0_in = """
2
3
1
2
4
10
100"""

case0_out = """
2 3 4
30 120 210 300"""
cases.append((case0_in, case0_out))


def test_cases():
    global cases
    for i, (_in, _out) in enumerate(cases):
        yield check_case, _in.strip(), _out.strip()


def check_case(_in, _out):
    actual = main(_in.split("\n"))
    actual = actual if isinstance(actual, list) else [actual]
    expected = _out.split("\n")
    assert_equals(actual, expected)