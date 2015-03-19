# coding=utf-8
import sys
from cStringIO import StringIO

import pytest

import solution


cases = []
case0_in = """
6
1 4 3 5 6 2
"""

case0_out = """
1 2 3 4 5 6
"""
cases.append((case0_in, case0_out))

case1_in = """
9
9 8 6 7 3 5 4 1 2
"""

case1_out = """
1 2 3 4 5 6 7 8 9
"""
cases.append((case1_in, case1_out))


@pytest.fixture(params=cases)
def case(request):
    return request.param


# noinspection PyShadowingNames
def test_cases(case, capsys):
    actual, expected = map(str.lstrip, case)
    sys.stdin = StringIO(actual)
    solution.main()
    out, _ = capsys.readouterr()
    sys.stdin = sys.__stdin__

    assert out == expected
