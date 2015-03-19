from random import Random
import nose.tools as test
import solution


cases = []
case0_in = """
4
1
3
5
11"""

case0_out = """
-1
555
33333
55555533333"""
cases.append((case0_in, case0_out))

case1_in = """
6
15
16
17
19
21
22"""

case1_out = """
555555555555555
5555553333333333
55555555555533333
5555555553333333333
555555555555555555555
5555555555553333333333"""
cases.append((case1_in, case1_out))

case2_in = """
_
1
2
"""

case2_out = """
-1
-1"""
cases.append((case2_in, case2_out))

case3_in = """
1
99999"""

case3_out = '5' * 99999
cases.append((case3_in, case3_out))


def test_cases():
    global cases
    for i, (_in, _out) in enumerate(cases):
        yield check_case, _in.strip(), _out.strip()


def check_case(_in, _out):
    _in = [item.strip() for item in _in.split("\n")]
    _in = map(str, solution.main(_in))
    _out = [item.strip() for item in _out.split("\n")]
    test.assert_equal(_in, _out)
    test.assert_equal("\n".join(_in), "\n".join(_out))


def test_edge_small():
    T = 1
    rand_case = [T]
    for _ in xrange(T):
        N = 1
        rand_case.append(N)
    test.assert_equal(map(str, solution.main(rand_case)), ['-1'])


def test_edge_large():
    _random = Random(1)

    T = 20
    rand_case = [T]
    for _ in xrange(T):
        N = _random.randint(1, 100000)
        rand_case.append(N)
    test.assert_is_not_none(map(str, solution.main(rand_case)))


def test_edge_large_2():
    _random = Random(1)

    T = 20
    rand_case = [T]
    for _ in xrange(T):
        N = _random.randint(10000, 100000)
        rand_case.append(N)
    test.assert_is_not_none(map(str, solution.main(rand_case)))

