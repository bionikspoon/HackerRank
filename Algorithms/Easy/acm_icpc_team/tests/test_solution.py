from nose.tools import *

cases = []
case0_in = """
4 5
10101
11100
11010
00101"""

case0_out = """
5
2"""
cases.append((case0_in, case0_out))



def test_cases():
    global cases
    for i, (_in, _out) in enumerate(cases):
        yield check_case, "case %i" % i, _in.strip(), _out.strip()


# noinspection PyUnusedLocal
def check_case(name, _in, _out):
    actual = main(_in.split("\n"))
    actual = actual if isinstance(actual, list) else [actual]
    expected = _out.split("\n")
    assert_equals(actual, expected)