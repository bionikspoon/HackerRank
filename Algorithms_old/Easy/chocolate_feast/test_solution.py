from nose.tools import *
from solution import *

cases = []
case0_in = """
3
10 2 5
12 4 4
6 2 2"""

case0_out = """
6
3
5"""
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


