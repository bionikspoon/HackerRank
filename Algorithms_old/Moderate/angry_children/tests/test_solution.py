from random import *

from nose.tools import *

cases = []
case0_in = """
7
3
10
100
300
200
1000
20
30"""

case0_out = """
20"""
cases.append((case0_in, case0_out))

case1_in = """
10
4
1
2
3
4
10
20
30
40
100
200"""

case1_out = """
3"""
cases.append((case1_in, case1_out))

case2_in = """
6
3
10
20
30
100
101
102"""

case2_out = """
2"""
cases.append((case2_in, case2_out))


def test_cases():
    global cases
    for i, (_in, _out) in enumerate(cases):
        yield check_case, "case %i" % i, _in.strip(), _out.strip()


# noinspection PyUnusedLocal
def check_case(name, _in, _out):
    _list = map(int, _in.split("\n"))
    n = _list.pop(0)
    k = _list.pop(0)
    actual = main(n, k, _list)
    actual = actual if isinstance(actual, list) else [actual]
    expected = _out.split("\n")
    assert_equals(actual, expected)


def test_random_case_1():
    _random = Random(1)
    n = _random.randint(2, 10 ** 5)
    k = _random.randint(2, n)
    list_n = [_random.randint(0, 10 ** 9) for _ in xrange(n)]
    assert_equals(main(n, k, list_n), "847525142")


def test_random_case_2_random_k():
    _random = Random(1)
    n = 10 ** 5
    k = _random.randint(2, n)
    list_n = [_random.randint(10 ** 8, 10 ** 9) for _ in xrange(n)]
    assert_equals(main(n, k, list_n), "118315011")


def test_random_case_2_small_k():
    _random = Random(1)
    n = 10 ** 5
    k = 2
    list_n = [_random.randint(10 ** 8, 10 ** 9) for _ in xrange(n)]
    assert_equals(main(n, k, list_n), "0")


def test_random_case_2_large_k():
    _random = Random(1)
    n = 10 ** 5
    k = 10 ** 5 - 2
    list_n = [_random.randint(10 ** 8, 10 ** 9) for _ in xrange(n)]
    assert_equals(main(n, k, list_n), "899946401")


def test_random_case_2_medium_k():
    _random = Random(1)
    n = 10 ** 5
    k = 10 ** 5 // 2
    list_n = [_random.randint(10 ** 8, 10 ** 9) for _ in xrange(n)]
    assert_equals(main(n, k, list_n), "447523575")